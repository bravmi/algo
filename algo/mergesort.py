import random


def merge(left: list[float], right: list[float]) -> list[float]:
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def mergesort(a: list[float]) -> list[float]:
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)


def test10():
    a = [random.randrange(0, 10) for _ in range(10)]
    b = mergesort(a)
    assert b == sorted(a)


if __name__ == '__main__':
    a: list[float] = [random.randrange(0, 10) for _ in range(10)]
    print('before sort:')
    print(a)
    b = mergesort(a)
    print('after sort:')
    print(b)
