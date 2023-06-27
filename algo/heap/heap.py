class Heap:
    """A min-heap implementation."""

    def __init__(self, values: list[float] | None = None):
        self._values = []
        if values:
            self._values = values.copy()
            self._heapify()

    def values(self) -> list[float]:
        return self._values

    def _parent(self, i) -> int:
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    def root(self) -> float:
        return self[0]

    def push(self, value: float) -> None:
        self._values.append(value)
        self._sift_up(len(self) - 1)

    def _sift_up(self, i: int) -> None:
        if i <= 0:
            return
        j = self._parent(i)
        if self[j] > self[i]:
            self[i], self[j] = self[j], self[i]
            self._sift_up(j)

    def pop(self) -> float:
        last = self._values.pop()
        if not self._values:
            return last
        root, self[0] = self[0], last
        self._sift_down(0)
        return root

    def push_pop(self, value: float) -> float:
        if not self._values or value < self[0]:
            return value
        root, self[0] = self[0], value
        self._sift_down(0)
        return root

    def _sift_down(self, i: int) -> None:
        l = self._left_child(i)
        r = self._right_child(i)
        _, j = min(
            (self[i], i),
            (self[l], l),
            (self[r], r),
        )
        if j != i:
            self[i], self[j] = self[j], self[i]
            self._sift_down(j)

    def _heapify(self) -> None:
        """Heapify the array in O(n) time."""
        for i in range(len(self) // 2, -1, -1):
            self._sift_down(i)

    def __getitem__(self, i: int) -> float:
        if i >= len(self):
            return float('inf')
        return self._values[i]

    def __setitem__(self, i: int, value: float) -> None:
        self._values[i] = value

    def __len__(self) -> int:
        return len(self._values)

    def __str__(self) -> str:
        return str(self._values)

    def __repr__(self) -> str:
        return str(self)


if __name__ == '__main__':
    h = Heap([3, 2])
    assert h.root() == 2
    assert h.values() == [2, 3]
