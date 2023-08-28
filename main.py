from pathlib import Path
from shutil import copyfile
from threading import Thread
import argparse
import logging
from uuid import uuid4


def get_params():
    args_cli = argparse.ArgumentParser(description="File sorter")
    args_cli.add_argument("-s", "--source", required=True)
    args_cli.add_argument("-o", "--output", default="sort_result")
    return vars(args_cli.parse_args())


def sort_folder(folder : Path, output: Path):
    for el in folder.iterdir():
        if el.is_file():
            ext = el.suffix
            if not ext:
                continue
            destination_path = output.joinpath(ext[1:])
            destination_path.mkdir(exist_ok=True, parents=True)
            logging.info(f"In thread created {ext}")
            destination_file = destination_path.joinpath(el.name)
            if destination_file.exists():
                destination_file = destination_path.joinpath(f"{el.stem}_{uuid4()}{el.suffix}")
            try:
                copyfile(el, destination_file)
            except OSError as e:
                logging.error(e)

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
    output_path = Path(output)
    threads = []
    for folder in folders:
        th = Thread(target=sort_folder, args=(folder, output_path))
        th.start()
        threads.append(th)
    logging.info(f"Wait all {len(threads)} threads")
    [th.join() for th in threads]
    logging.info("Finish")
    print(folders)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    args = get_params()
    main(args_cli=args)