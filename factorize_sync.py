from multiprocessing import cpu_count, Pool, current_process


def factorize_one(n):
    result_div = []
    for i in range(1, n + 1):
        if n % i == 0:
            result_div.append(i)
    return result_div


def factorize_mul_pool(*number):
    result: list[list[int]] = []
    # for n in number:
    with Pool(processes=cpu_count()) as pool:
        # result_div = factorize_one(n , max_number)
        result = pool.map(factorize_one, number)
        #result.append(result_div)
    return tuple(result)


def factorize_mul(*number):
    result: list[list[int]] = []
    for n in number:
        result_div = factorize_one(n)
        result.append(result_div)
    return tuple(result)


def factorize(*number):
    result: list[list[int]] = []
    for n in number:
        result_div = []
        for i in range(1,n+1):
            if n % i == 0:
                result_div.append(i)
        result.append(result_div)
    return tuple(result)


def test_factorize():
    a, b, c, d = factorize_mul(128, 255, 99999, 10651060)
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


if __name__ == "__main__":
    test_factorize()
