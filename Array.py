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


def test3():
    a = Array([1, 2, 3])

    assert a._array == [1, 2, 3, None]
    assert a._nval == 3
    assert a._max == 4
    assert a.index(3) == 2

    a.remove(1)
    assert a.index(3) == 1
    assert a._array == [2, 3, 3, None]
    assert a._nval == 2
    assert a._max == 4


def test_dunders():
    import pytest

    a = Array()
    a.append(1)
    a.append(2)
    a.append(3)

    assert a[2] == 3
    assert a.tolist() == [1, 2, 3]
    assert str(a) == '[1, 2, 3]'
    assert 2 in a
    assert None not in a
    assert -1 not in a

    assert a[0:2] == [1, 2]
    with pytest.raises(TypeError):
        a[2:4] = [3, 4]


if __name__ == '__main__':
    pass
