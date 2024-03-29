"""
Iterative in-place version
"""
import random


def partition(a: list[float], start: int, stop: int) -> int:
    """Returns eventual index of a pivot"""

    n = stop - start
    p = start + random.randrange(n)
    a[start], a[p] = a[p], a[start]

    last = start
    for i in range(start, stop):
        if a[i] < a[start]:
            last += 1
            a[last], a[i] = a[i], a[last]
    a[start], a[last] = a[last], a[start]
    return last


def quicksort(a: list[float]) -> list[float]:
    stack = [(0, len(a))]

    while stack:
        start, stop = stack.pop()
        n = stop - start
        if n <= 1:
            continue

        p = partition(a, start, stop)
        stack.append((start, p))
        stack.append((p + 1, stop))
    return a


def test10() -> None:
    a: list[float] = [random.randrange(0, 10) for _ in range(10)]
    quicksort(a)
    assert a == sorted(a)


if __name__ == '__main__':
    a: list[float] = [random.randrange(0, 10) for _ in range(10)]
    print('before sort:')
    print(a)
    quicksort(a)
    print('after sort:')
    print(a)
