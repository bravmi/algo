import random


def bubblesort(a: list) -> list:
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                is_sorted = False
    return a


def test10():
    a = [random.randrange(0, 10) for _ in range(10)]
    b = bubblesort(a)
    assert b == sorted(a)


if __name__ == '__main__':
    a = [random.randrange(0, 10) for _ in range(10)]
    print('before sort:')
    print(a)
    b = bubblesort(a)
    print('after sort:')
    print(b)
