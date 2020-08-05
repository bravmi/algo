import pytest

from .Array import NGROW, NINIT, Array


def test_tolist():
    a = Array([1, 2, 3])
    assert a.tolist() == [1, 2, 3]


def test_str():
    a = Array([1, 2, 3])
    assert str(a) == '[1, 2, 3]'


def test_repr():
    a = Array([1, 2, 3])
    assert repr(a) == '[1, 2, 3]'


def test_contains():
    a = Array([1, 2, 3])
    assert 2 in a
    assert None not in a
    assert -1 not in a


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


def test_index():
    a = Array([1, 2, 3])
    assert a.index(2) == 1

    with pytest.raises(ValueError):
        a.index(4)


def test_clear():
    a = Array([1, 2, 3])
    assert len(a) == 3
    a.clear()
    assert len(a) == 0


def test_getitem():
    a = Array([1, 2, 3])
    assert a[1] == 2

    with pytest.raises(IndexError):
        a[3]


def test_setitem():
    a = Array([1, 2, 3])
    a[2] = 2
    assert a[1:3] == [2, 2]

    with pytest.raises(IndexError):
        a[3] = 4
    with pytest.raises(TypeError):
        a[2:4] = [3, 4]


def test_remove():
    a = Array([1, 2, 3])
    a.remove(2)
    assert a.tolist() == [1, 3]


def test_init():
    a = Array([1, 2, 3])
    assert a.tolist() == [1, 2, 3]


def test_extend():
    a = Array()
    a.extend([1, 2, 3])
    assert a.tolist() == [1, 2, 3]


def test_append():
    a = Array()
    a.append(1)
    a.append(2)
    a.append(3)
    assert a.tolist() == [1, 2, 3]


def test_grow():
    a = Array(range(0, NINIT))
    x = NINIT
    a.append(x)
    assert len(a) == NINIT * NGROW
