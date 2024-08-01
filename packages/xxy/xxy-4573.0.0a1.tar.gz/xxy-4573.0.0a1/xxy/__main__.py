import argparse
import asyncio
import logging
import sys

from loguru import logger

from xxy.__about__ import __version__
from xxy.agent import build_table
from xxy.config import load_config
from xxy.data_source.folder import FolderDataSource


def config_log_level(v: int) -> None:
    logger.remove()
    log_format = "{message}"
    if v >= 4:
        logger.add(sys.stderr, level="TRACE", format=log_format)
    elif v >= 3:
        logger.add(sys.stderr, level="DEBUG", format=log_format)
    elif v >= 2:
        logger.add(sys.stderr, level="INFO", format=log_format)
    elif v >= 1:
        logger.add(sys.stderr, level="SUCCESS", format=log_format)
    else:
        logger.add(sys.stderr, level="WARNING", format=log_format)

    if v < 4:
        # avoid "WARNING! deployment_id is not default parameter."
        langchain_logger = logging.getLogger("langchain.chat_models.openai")
        langchain_logger.disabled = True


async def amain() -> None:
    parser = argparse.ArgumentParser(description="xxy-" + __version__)
    parser.add_argument("-v", action="count", default=0, help="verbose level.")
    parser.add_argument(
        "-c",
        default="",
        help="Configuration file path. if not provided, use `~/.xxy_cfg.json` .",
    )
    parser.add_argument(
        "--gen_cfg",
        action="store_true",
        help="Regenerate config from environment variables.",
    )
    parser.add_argument(
        "folder_path",
        help="Folder path to search for documents.",
    )
    parser.add_argument(
        "-t",
        nargs="*",
        help="Target company",
    )
    parser.add_argument(
        "-d",
        nargs="+",
        help="Report date",
    )
    parser.add_argument(
        "-n",
        nargs="+",
        help="Entity name",
    )
    args = parser.parse_args()

    config_log_level(args.v)

    config = load_config(gen_cfg=args.gen_cfg)
    data_source = FolderDataSource(args.folder_path)
    await build_table(data_source, args.t, args.d, args.n)


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    main()
