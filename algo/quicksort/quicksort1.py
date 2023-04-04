"""
Recursive and not in-place but very readable version
"""
import random


def quicksort(a: list[float]) -> list[float]:
    if len(a) <= 1:
        return a

    less, equal, greater = [], [], []

    pivot = random.choice(a)
    for x in a:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)

    return quicksort(less) + equal + quicksort(greater)


def test10():
    a = [random.randrange(0, 10) for _ in range(10)]
    b = quicksort(a)
    assert b == sorted(a)


if __name__ == '__main__':
    a: list[float] = [random.randrange(0, 10) for _ in range(10)]
    print('before sort:')
    print(a)
    b = quicksort(a)
    print('after sort:')
    print(b)
