import pytest

from .Array import Array


def test_basic():
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


def test_reverse():
    a = Array([1, 2, 3, 4, 5])
    a.reverse()
    assert a.tolist() == [5, 4, 3, 2, 1]


def test_rotate():
    a = Array([1, 2, 3, 4, 5])
    a.rotate(2)
    assert a.tolist() == [4, 5, 1, 2, 3]
    a.rotate(2, left=True)
    assert a.tolist() == [1, 2, 3, 4, 5]
