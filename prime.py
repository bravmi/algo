import collections as co


def factors(n: int) -> dict[int, int]:
    res: dict = co.defaultdict(lambda: 0)
    i = 2
    while i * i <= n:
        if n % i == 0:
            res[i] += 1
            n //= i
        else:
            i += 1
    if n != 1:
        res[n] += 1
    return dict(res)


def tests():
    assert factors(13195) == {5: 1, 7: 1, 13: 1, 29: 1}
    assert factors(600851475143) == {71: 1, 839: 1, 1471: 1, 6857: 1}


if __name__ == '__main__':
    tests()
