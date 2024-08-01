from typing import Any, Awaitable, List, Optional

from loguru import logger

from xxy.contract import Entity, Query
from xxy.data_source.base import DataSourceBase
from xxy.selector import select_entity


async def build_table(
    data_source: DataSourceBase, companys: List[str], dates: List[str], names: List[str]
) -> None:
    companys_to_search = companys if len(companys) > 0 else ["any"]
    for company in companys_to_search:
        for date in dates:
            for name in names:
                query = Query(company=company, date=date, entity_name=name)
                candidates = await data_source.search(query)
                logger.trace(f"Candidates for: {query}")
                for candidate in candidates:
                    logger.trace(f"ref {candidate.reference}, value: {candidate.value}")
                print(await select_entity(query, candidates))
