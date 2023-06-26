class Heap:
    def __init__(self, values: list | None = None):
        self._values = []
        if values:
            self._values = values.copy()
            self._heapify()

    def values(self) -> list:
        return self._values

    def _parent(self, i) -> int:
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    def root(self):
        return self._values[0]

    def push(self, value) -> None:
        self._values.append(value)
        self._sift_up(len(self._values) - 1)

    def _sift_up(self, i: int) -> None:
        if i == 0:
            return
        j = self._parent(i)
        if self._values[j] > self._values[i]:
            self._values[i], self._values[j] = (
                self._values[j],
                self._values[i],
            )
            self._sift_up(j)

    def pop(self):
        last = self._values.pop()
        if not self._values:
            return last
        root, self._values[0] = self._values[0], last
        self._sift_down(0)
        return root

    def push_pop(self, value) -> int:
        if not self._values or value < self._values[0]:
            return value
        root, self._values[0] = self._values[0], value
        self._sift_down(0)
        return root

    def _sift_down(self, i: int) -> None:
        l = self._left_child(i)
        r = self._right_child(i)
        j = i
        if l < len(self._values) and self._values[l] < self._values[j]:
            j = l
        if r < len(self._values) and self._values[r] < self._values[j]:
            j = r
        if j != i:
            self._values[i], self._values[j] = (
                self._values[j],
                self._values[i],
            )
            self._sift_down(j)

    def _heapify(self) -> None:
        """Heapify the array in O(n) time."""
        for i in range(len(self._values) // 2, -1, -1):
            self._sift_down(i)

    def __len__(self) -> int:
        return len(self._values)

    def __str__(self):
        return str(self._values)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    h = Heap([3, 2])
    assert h.root() == 2
    assert h.values() == [2, 3]
