from pathlib import Path
from shutil import copyfile
from threading import Thread, Semaphore
import argparse
import logging
from typing import Any
from uuid import uuid4
from datetime import datetime
from factorize_sync import test_factorize


def get_params():
    args_cli = argparse.ArgumentParser(description="File sorter")
    args_cli.add_argument(
        "-s", "--source", required=False, default="pictures", help="default: pictures"
    )
    args_cli.add_argument("-o", "--output", default="sort_result")
    args_cli.add_argument(
        "-t", "--threads", default=10, type=int, help="Max threads, default: 10"
    )
    args_cli.add_argument("-v", "--verbose", action="store_true")
    args_cli.add_argument("-f", "--factorize", action="store_true")

    return vars(args_cli.parse_args())


def sort_folder(
    folder: Path, output: Path, condition: Semaphore, verbose: bool = False
) -> None:
    with condition:
        if verbose:
            logging.info(f"`Thread running for sort in {folder}")
        # pre sorting files to dict
        result = {}
        for el in folder.iterdir():
            if el.is_file():
                ext = el.suffix.lower()
                if not ext:
                    continue
                ext_items = result.get(ext, [])
                ext_items.append(el)
                result[ext] = ext_items
        # physical copy founded files
        for ext, ext_items in result.items():
            destination_path = output.joinpath(ext[1:])
            destination_path.mkdir(exist_ok=True, parents=True)
            for el in ext_items:
                destination_file = destination_path.joinpath(el.name)
                if destination_file.exists():
                    destination_file = destination_path.joinpath(
                        f"{el.stem}_{uuid4()}{el.suffix}"
                    )
                try:
                    if verbose:
                        logging.info(f"`Thread copy {el} to {destination_file}")
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
    threads_maximum: int = args_cli.get("threads", 10)
    verbose = args_cli.get("verbose", False)

    assert source is not None, "Source must be defined"
    if verbose:
        logging.info("Start search")
    folders = get_folders(Path(source))
    output_path = Path(output)
    threads = []
    pool = Semaphore(threads_maximum)
    for num, folder in enumerate(folders):
        th = Thread(
            name=f"Th-{num}",
            target=sort_folder,
            args=(folder, output_path, pool, verbose),
        )
        th.start()
        threads.append(th)
    if verbose:
        logging.info(f"Wait all {len(threads)} threads")
    [th.join() for th in threads]
    if verbose:
        logging.info("Finish")
    # print(folders)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s [ %(threadName)s ] %(message)s"
    )
    args = get_params()
    threads_max = args.get("threads", 10)
    factorize = args.get("factorize", False)
    start_time = datetime.now()
    if factorize:
        test_factorize()
    else:
        main(args_cli=args)
    duration = datetime.now() - start_time
    logging.info(f"Duration : {duration} with threads: {threads_max}")
