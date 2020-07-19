"""
Regular binary search
"""


def binsearch(x, a):
    low, high = 0, len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        elif a[mid] == x:
            return mid
    return None


def test10():
    a = [1, 1, 2, 2, 2, 2, 3, 4, 7, 8, 9]
    assert binsearch(2, a) == 5


def test4():
    a = [1, 1, 1, 1]
    assert binsearch(1, a) == 1
    assert binsearch(2, a) is None


def test3():
    a = [1, 2, 3]
    assert binsearch(2, a) == 1
    assert binsearch(2.5, a) is None


if __name__ == '__main__':
    x = 2
    a = [1, 1, 2, 2, 2, 2, 3, 4, 7, 8, 9]
    print('x = {}'.format(x))
    print('a = {}'.format(a))
    print(binsearch(x, a))
