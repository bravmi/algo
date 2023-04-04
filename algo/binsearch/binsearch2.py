"""
My take on binary search with ranges of the same elements
"""
from typing import Callable


def binsearch(x, a: list[int], cmp: Callable[[int, int], bool]) -> int | None:
    low, high = 0, len(a)

    while low < high:
        mid = (low + high) // 2
        if cmp(a[mid], x):
            low = mid + 1
        else:
            high = mid
    return low


def test10():
    a = [1, 1, 2, 2, 2, 2, 3, 4, 7, 8, 9]
    assert binsearch(2, a, cmp=lambda x, y: x <= y) == 6


def test4():
    a = [1, 1, 1, 1]
    assert binsearch(1, a, cmp=lambda x, y: x < y) == 0
    assert binsearch(1, a, cmp=lambda x, y: x <= y) == 4
    assert binsearch(2, a, cmp=lambda x, y: x < y) == 4
    assert binsearch(2, a, cmp=lambda x, y: x <= y) == 4


def test3():
    a = [1, 2, 3]
    assert binsearch(2, a, cmp=lambda x, y: x < y) == 1
    assert binsearch(2, a, cmp=lambda x, y: x <= y) == 2
    assert binsearch(2.5, a, cmp=lambda x, y: x < y) == 2
    assert binsearch(2.5, a, cmp=lambda x, y: x <= y) == 2


if __name__ == '__main__':
    x = 2
    a = [1, 1, 2, 2, 2, 2, 3, 4, 7, 8, 9]
    print(f'x = {x}')
    print(f'a = {a}')
    print(binsearch(x, a, lambda x, y: x <= y))
    print(binsearch(x, a, lambda x, y: x < y))
