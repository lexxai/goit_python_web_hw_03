from pathlib import Path
from shutil import copyfile
from threading import Thread, Semaphore
import argparse
import logging
from typing import Any, Tuple
from uuid import uuid4
from datetime import datetime
from multiprocessing import cpu_count
from factorize_sync import factorize_mul, factorize_mul_thread, factorize_mul_pool, factorize_sync
from factorize_async_pipe import factorize_mul_pipe


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

def test_factorize(method: int = 0):
    source = (128, 255, 99999, 10651060)

    if method == 0:
        a, b, c, d = factorize_sync(*source)
    elif method == 1:
        a, b, c, d = factorize_mul(*source)
    elif method == 2:
        a, b, c, d = factorize_mul_pool(*source)
    elif method == 3:
        threads_maximum  = 10
        logging.info(
            f"Threads max: {threads_maximum}"
        )
        a, b, c, d = factorize_mul_thread(*source, threads_maximum = threads_maximum)

    elif method == 4:
        a, b, c, d = factorize_mul_pipe(*source)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]



def test_fact():
    METHOD_DESC: tuple = ('SYNC ONE FUNC', 'SYNC SPLIT FUNC', "ASYNC MP POOL", "ASYNC THREAD", "ASYNC MP PROC PIPE")
    durations = []
    cpu_total_m = cpu_count()
    for method in range(0,len(METHOD_DESC)):
        start_time_m = datetime.now()
        test_factorize(method)
        duration_m = datetime.now() - start_time_m
        durations.append(duration_m)
        logging.info(
            f"Method [{METHOD_DESC[method]}]. Duration: {duration_m}  on this system is total cpu: {cpu_total_m}"
        )

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s [ %(threadName)s ] %(message)s"
    )
    args = get_params()
    threads_max = args.get("threads", 10)
    factorize = args.get("factorize", False)

    if factorize:
        test_fact()
    else:
        cpu_total = cpu_count()
        start_time = datetime.now()
        main(args_cli=args)
        duration = datetime.now() - start_time
        logging.info(
            f"Duration : {duration} with max threads: {threads_max}, on this system is total cpu: {cpu_total}"
        )
