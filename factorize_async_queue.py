from multiprocessing import Queue, Process, current_process
from time import sleep
import sys
import logging

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)




def worker(Queue: Queue):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = Queue.get()
    logger.debug(val**2)
    sys.exit(0)


def factorize_one_queue(queue: Queue) -> None:
    name = current_process().name
    # logger.debug(f'{name} started...')
    idx, n = queue.get()
    # logger.debug(f'{name} received ... {n}')
    result_div = []
    for i in range(1, n + 1):
        if n % i == 0:
            result_div.append(i)
    queue.put((idx, result_div))
    sys.exit(0)


def factorize_mul_queue(*number: object) -> tuple[list[int]]:
    result: list[list[int]] = []
    recipients = []
    senders = []
    processes = []
    q = Queue()
    for _ in number:
        w = Process(target=factorize_one_queue, args=(q,))
        w.start()
        processes.append(w)
    # send tasks
    for n in enumerate(number):
        q.put(n)

    [p.join() for p in processes]

    # get results
    for _ in processes:
        idx, res = q.get()
        result.append(res)
    return tuple(result)


def test_factorize(method: int = 0):
    source = (128, 255, 99999, 10651060)

    if method == 0:
        a, b, c, d = factorize_mul_queue(*source)

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

def test_less():
    recipient1, sender1 = Pipe()
    recipient2, sender2 = Pipe()

    w1 = Process(target=worker, args=(recipient1, ))
    w2 = Process(target=worker, args=(recipient2, ))

    w1.start()
    w2.start()

    sender1.send(8)
    sleep(1)
    sender2.send(16)

if __name__ == '__main__':
    test_factorize()
    # test_less()

