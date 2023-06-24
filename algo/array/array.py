"""
Dynamic array in python of all things
"""
NINIT = 1
NGROW = 2


class Array:
    def __init__(self, iterable=None):
        self._nval = 0
        self._array = [None] * NINIT
        self._max = NINIT

        if iterable:
            self.extend(iterable)

    def extend(self, iterable) -> None:
        for v in iterable:
            self.append(v)

    def append(self, value) -> None:
        if self._nval >= self._max:
            array = [None] * (NGROW * self._max)
            array[: self._nval] = self._array
            self._array = array
            self._max *= NGROW

        self._array[self._nval] = value
        self._nval += 1

    def remove(self, value) -> None:
        i = self.index(value)
        self._array[i : self._nval - 1] = self._array[i + 1 : self._nval]
        self._nval -= 1

    def index(self, value) -> int:
        for i in range(self._nval):
            if self._array[i] == value:
                return i
        raise ValueError

    def clear(self) -> None:
        self._nval = 0

    def tolist(self) -> list:
        return [v for v in self]

    def reverse(self) -> None:
        self._reverse(0, self._nval)

    def _reverse(self, start: int, stop: int) -> None:
        a = self._array
        i = start
        j = stop - 1
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    def rotate(self, k: int, left=False) -> None:
        """
        in-place
        :param k: rotation offset
        :param left: rotate left if True, right otherwise
        """
        n = self._nval
        k = k % n
        if left:
            self._reverse(0, k)
            self._reverse(k, n)
            self._reverse(0, n)
        else:
            self._reverse(0, n)
            self._reverse(0, k)
            self._reverse(k, n)

    def __getitem__(self, index: int):
        if isinstance(index, int) and not 0 <= index < self._nval:
            raise IndexError
        return self._array[index]

    def __setitem__(self, index: int, value) -> None:
        if isinstance(index, slice):
            raise TypeError('set index must be an int')
        if not 0 <= index < self._nval:
            raise IndexError
        self._array[index] = value

    def __len__(self) -> int:
        return self._nval

    def __iter__(self):
        for i in range(self._nval):
            yield self._array[i]

    def __contains__(self, value) -> bool:
        for x in self:
            if x == value:
                return True
        return False

    def __str__(self) -> str:
        return '[{}]'.format(', '.join(str(x) for x in self))

    def __repr__(self) -> str:
        return str(self)


if __name__ == '__main__':
    pass
