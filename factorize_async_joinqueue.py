from multiprocessing import JoinableQueue, Process, current_process
from time import sleep
import sys
import logging
import random

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)


def factorize_one_jqueue(jqueue: JoinableQueue, result_jq: JoinableQueue) -> None:
    name = current_process().name
    # logger.debug(f'{name} started...')
    idx, n = jqueue.get()
    # logger.debug(f'{name} received ... {n}')
    result_div = []
    for i in range(1, n + 1):
        if n % i == 0:
            result_div.append(i)
    # sleep(random.randrange(1,5))
    result_jq.put((idx, result_div))
    jqueue.task_done()
    sys.exit(0)


def factorize_mul_jqueue(*number: object) -> tuple[list[int]]:
    result: list[list[int]] = []
    processes = []
    jq = JoinableQueue()
    res_jq = JoinableQueue()
    for n in enumerate(number):
        w = Process(target=factorize_one_jqueue, args=(jq, res_jq))
        w.start()
        processes.append(w)
        jq.put(n)
    # send tasks
    #for n in enumerate(number):
    #   jq.put(n)

    jq.join()
    # print("JQ DONE")
    # get results
    for _ in processes:
        idx, res = res_jq.get()
        result.insert(idx,res)
    return tuple(result)


def test_factorize(method: int = 0):
    source = (128, 255, 99999, 10651060)

    if method == 0:
        a, b, c, d = factorize_mul_jqueue(*source)

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
    print("All ok")


if __name__ == "__main__":
    test_factorize()
