def kadane(a):
    """Kadane's algo for maximum sum subarray problem

    O(n) time, O(1) space
    """
    best = curr = 0
    for x in a:
        curr = max(curr + x, 0)
        best = max(best, curr)
    return best


def test():
    assert kadane([3, 4, 5]) == 12
    assert kadane([4, -2, -8, 5, -2, 7, 7, 2, -6, 5]) == 19
    assert kadane([-2, -3, -5]) == 0


if __name__ == '__main__':
    pass
