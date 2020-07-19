import random


def selectionsort(a):
    """O(n^2) time, O(1) space"""
    n = len(a)
    for i in range(n):
        _, smallest = min((a[j], j) for j in range(i, n))
        a[i], a[smallest] = a[smallest], a[i]
    return a


def test10():
    a = [random.randrange(0, 10) for _ in range(10)]
    b = selectionsort(a)
    assert b == sorted(a)


if __name__ == '__main__':
    pass
