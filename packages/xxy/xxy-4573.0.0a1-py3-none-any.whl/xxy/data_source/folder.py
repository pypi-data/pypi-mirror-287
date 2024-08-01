from pathlib import Path
from typing import Dict, List, Optional

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from llama_index.core import VectorStoreIndex
from llama_index.core.schema import Document
from llama_index.core.settings import Settings
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.readers.file import PDFReader
from loguru import logger

from xxy.client import get_slm
from xxy.config import load_config
from xxy.contract import Entity, Query
from xxy.data_source.base import DataSourceBase


class IndexCache:
    def __init__(self) -> None:
        pass

    async def get_index(self, select_file: Path) -> VectorStoreIndex:
        logger.trace("get_index for {}", select_file)
        index_path = select_file.with_suffix(".index")
        if index_path.exists():
            logger.trace("load index from cache: {}", index_path)
            raise NotImplementedError("Index cache not implemented")
        else:
            logger.trace("load index from scratch: {}", select_file)
            index = await self._get_index(select_file)
            # save index
            return index

    async def _get_index(self, select_file: Path) -> VectorStoreIndex:
        config = load_config()
        documents = PDFReader().load_data(select_file, {"file_path": str(select_file)})
        embed = AzureOpenAIEmbedding(
            azure_endpoint=config.llm.openai_api_base,
            azure_deployment=config.llm.embedding.deployment_id,
            api_key=config.llm.openai_api_key,
            api_version=config.llm.openai_api_version,
        )
        Settings.embed_model = embed
        parser = Settings.node_parser
        nodes = parser.get_nodes_from_documents(documents)
        logger.debug(f"Loaded {len(nodes)} document nodes from {select_file}")
        return VectorStoreIndex(nodes=nodes, settings=Settings)


class FolderDataSource(DataSourceBase):
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.index_cache = IndexCache()

    async def search(self, query: Query) -> List[Entity]:
        files = await self.select_file(query)
        logger.info("selected file: {}", files)
        index = await self.index_cache.get_index(files)
        self.query_engine = index.as_retriever()
        response = self.query_engine.retrieve(query.entity_name)
        return [
            Entity(
                value=node.text,
                reference=node.metadata["file_path"]
                + ":"
                + node.metadata["page_label"],
            )
            for node in response
        ]

    async def select_file(self, query: Query) -> Path:
        candidates = list(Path(self.folder_path).glob("**/*.pdf", case_sensitive=False))
        selector = (
            ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        (
                            "User gives a list of financial reports to search for infomation of a company. Please select the one that with following rule:\n"
                            '- output should be formatted as JSON like {{"index": 1, "reason": ""}}\n'
                            "- the index should be the same as user given, and the reason is a string to explain why\n"
                        ),
                    ),
                    (
                        "human",
                        "Search report about company {company} for {date}\n\nHere are the candidates:\n{candidates}",
                    ),
                ]
            )
            | get_slm()
            | JsonOutputParser()
        )

        candidates_desc = "\n".join(
            [f"index: {ix}, file_name: {i}" for ix, i in enumerate(candidates)]
        )

        llm_output = await selector.ainvoke(
            {
                "company": query.company,
                "date": query.date,
                "candidates": candidates_desc,
            }
        )
        selected_idx: int = llm_output.get("index", -1)

        if selected_idx == -1:
            raise ValueError(f"no report found: {llm_output.get('reason', '')}")

        return candidates[selected_idx]
