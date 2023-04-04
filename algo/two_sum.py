def two_sum(nums: list[int], target: int) -> list[int]:
    """
    O(n)
    """
    hist: dict[int, int] = {}

    for i, x in enumerate(nums):
        if target - x in hist:
            return [hist[target - x], i]
        hist[x] = i
    return []


def test1():
    assert two_sum([1, 2, 3], 5) == [1, 2]


if __name__ == '__main__':
    pass
