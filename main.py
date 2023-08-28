from pathlib import Path
from threading import Thread
import argparse
import logging


def get_params():
    args_cli = argparse.ArgumentParser(description="File sorter")
    args_cli.add_argument("-s", "--source", required=True)
    args_cli.add_argument("-o", "--output", default="sort_result")
    return vars(args_cli.parse_args())


def get_folders(source_path: Path) -> list[Path]:
    folders = []
    for el in source_path.glob("*/**"):
        if el.is_dir():
            folders.append(el)
    return folders


def main(args_cli: dict = None):
    source = args_cli.get("source")
    output = args_cli.get("output", "sort_result")
    assert source is not None, "Source must be defined"
    logging.info("Start search")
    folders = get_folders(Path(source))
    print(folders)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    args = get_params()
    main(args_cli=args)