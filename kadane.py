def kadane(arr: list[float]) -> float:
    """Kadane's algo for maximum sum subarray problem

    O(n) time, O(1) space
    """
    best = curr = 0
    for x in arr:
        # two choices for max sum ending with x
        curr = max(curr + x, x)
        best = max(best, curr)
    return best


def tests():
    assert kadane([3, 4, 5]) == 12
    assert kadane([4, -2, -8, 5, -2, 7, 7, 2, -6, 5]) == 19
    assert kadane([-2, -3, -5]) == 0


def test_dojo():
    assert kadane([1, -3, 1, 2, -1]) == 3


def test_stackoverflow():
    assert kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


if __name__ == '__main__':
    tests()
