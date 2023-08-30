from pathlib import Path
from shutil import copyfile
from threading import Thread, Semaphore
import argparse
import logging
from uuid import uuid4
from datetime import datetime


def get_params():
    args_cli = argparse.ArgumentParser(description="File sorter")
    args_cli.add_argument("-s", "--source", required=True)
    args_cli.add_argument("-o", "--output", default="sort_result")
    return vars(args_cli.parse_args())


def sort_folder(folder : Path, output: Path, condition: Semaphore):
    with condition:
        logging.info(f"`Thread running for sort in {folder}")
        # pre sorting files to dict
        result = {}
        for el in folder.iterdir():
            if el.is_file():
                ext = el.suffix.lower()
                if not ext:
                    continue
                ext_items = result.get(ext,[])
                ext_items.append(el)
                result[ext] = ext_items
        # physical copy founded files
        for ext, ext_items in result.items():
            destination_path = output.joinpath(ext[1:])
            destination_path.mkdir(exist_ok=True, parents=True)
            for el in ext_items:
                destination_file = destination_path.joinpath(el.name)
                if destination_file.exists():
                    destination_file = destination_path.joinpath(f"{el.stem}_{uuid4()}{el.suffix}")
                try:
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
    assert source is not None, "Source must be defined"
    logging.info("Start search")
    folders = get_folders(Path(source))
    output_path = Path(output)
    threads = []
    pool = Semaphore(1)
    for num, folder in enumerate(folders):
        th = Thread(name=f'Th-{num}',  target=sort_folder, args=(folder, output_path, pool))
        th.start()
        threads.append(th)
    logging.info(f"Wait all {len(threads)} threads")
    [th.join() for th in threads]
    logging.info("Finish")
    # print(folders)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [ %(threadName)s ] %(message)s')
    args = get_params()
    start_time = datetime.now()
    main(args_cli=args)
    duration = datetime.now() - start_time
    logging.info(f"Duration : {duration}")