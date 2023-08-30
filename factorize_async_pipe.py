from multiprocessing import Pipe, Process, current_process
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)




def worker(pipe: Pipe):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = pipe.recv()
    logger.debug(val**2)
    sys.exit(0)


def factorize_one_pipe(pipe: Pipe) -> None:
    name = current_process().name
    # logger.debug(f'{name} started...')
    idx, n = pipe.recv()
    # logger.debug(f'{name} received ... {n}')
    result_div = []
    for i in range(1, n + 1):
        if n % i == 0:
            result_div.append(i)
    pipe.send((idx, result_div))
    sys.exit(0)


def factorize_mul_pipe(*number: object) -> tuple[list[int]]:
    result: list[list[int]] = []
    recipients = []
    senders = []
    processes = []
    for n in enumerate(number):
        sender, recipient = Pipe(duplex=True)
        recipients.append(recipient)
        senders.append(sender)
        w = Process(target=factorize_one_pipe, args=(recipient,))
        w.start()
        processes.append(w)
        # print("sending", n)
        sender.send(n)

    #g rab results
    for idx, sender in enumerate(senders):
        result.append(sender.recv()[1])
    # [p.join() for p in processes]
    return tuple(result)


def test_factorize(method: int = 0):
    source = (128, 255, 99999, 10651060)

    if method == 0:
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

