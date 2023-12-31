import concurrent.futures
from multiprocessing import cpu_count
import random
from time import sleep
import logging
import logging.config


# logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def factorize_one_concurrent(n: list[int]) -> list[int]:
    logger.debug(f'({__name__}) {n}')
    result_div = []
    for i in range(1, n + 1):
        if n % i == 0:   
            result_div.append(i)
    # sleep(random.randrange(1,5))
    return result_div


def factorize_mul_concurrent(*number: object) -> tuple[list[int]]:
    with concurrent.futures.ProcessPoolExecutor(cpu_count()) as executor:
        result: list[list] = executor.map(factorize_one_concurrent, number)
    return tuple(result)


def test_factorize(method: int = 0):
    source = (128, 255, 99999, 10651060)

    a, b, c, d = factorize_mul_concurrent(*source)

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
    logger.info("ALL OK")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s PID: %(process)d [ %(threadName)s ] %(message)s",
    )
    test_factorize()
