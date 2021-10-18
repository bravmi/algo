import pytest

from .list import *


def test_reversed():
    l = List()
    assert len(l) == 0
    a = [1, 2, 3]
    l.extend(a)
    assert l.to_array() == a
    assert l.reversed().to_array() == list(reversed(a))
    assert len(l) == 3
    l.clear()
    assert len(l) == 0


def test_remove():
    l = List()
    a = [1, 2, 3]
    for x in a:
        l.prepend(x)
    assert l.to_array() == list(reversed(a))
    assert l.reversed().to_array() == a
    assert len(l) == 3

    assert l.find(2).value == 2
    l.remove(2)
    assert len(l) == 2
    assert l.to_array() == [3, 1]
    l.remove(3)
    assert len(l) == 1
    assert l.to_array() == [1]
    l.remove(1)
    assert len(l) == 0
    assert l.to_array() == []


def test_copy():
    l = List()
    a = [1, 2, 3]
    l.extend(a)
    l2 = l.copy()
    l.remove(2)
    assert l.to_array() == [1, 3]
    assert l2.to_array() == [1, 2, 3]


def test_reverse():
    l = List()
    l.reverse()
    assert l.to_array() == []
    l.append(1)
    l.reverse()
    assert l.to_array() == [1]
    l.append(2)
    l.reverse()
    assert l.to_array() == [2, 1]
    l.prepend(3)
    l.reverse()
    assert l.to_array() == [1, 2, 3]


def test_sum_clear():
    l1 = List()
    l1.extend([1, 2, 3])
    l2 = List()
    l2.extend([4, 5, 6])
    assert l1.merge(l2).to_array() == [1, 2, 3, 4, 5, 6]
    assert (l1 + l2).to_array() == [1, 2, 3, 4, 5, 6]
    l1 += l2
    assert l1.to_array() == [1, 2, 3, 4, 5, 6]
    l2 = l1.copy()
    l1.clear()
    assert l1.to_array() == []
    l1 += l2
    assert l1.to_array() == [1, 2, 3, 4, 5, 6]


def test_get_set():
    l = List()
    l.extend([1, 2, 3])
    assert l[0] == 1
    assert l[1] == 2
    assert l[2] == 3
    with pytest.raises(IndexError):
        l[3] = 4
    assert l[-1] == 3
    assert l[-2] == 2
    assert l[-3] == 1
    with pytest.raises(IndexError):
        l[-4] = 0

    l[0] = 3
    l[1] = 2
    l[2] = 1
    assert l.to_array() == [3, 2, 1]


def test_contains_apply():
    l = List()
    a = [1, 2, 3]
    for x in a:
        l.append(x)
    assert 1 in l
    assert 2 in l
    assert 3 in l
    assert l.to_array() == [1, 2, 3]

    acc = []
    l.apply(lambda x: acc.append(x))
    assert acc == [1, 2, 3]


def test_inserts():
    l = List()
    l.append(1)
    l.insert_after(1, 2)
    l.insert_after(2, 3)
    assert l.to_array() == [1, 2, 3]

    l = List()
    l.append(3)
    l.insert_before(3, 2)
    l.insert_before(2, 1)
    assert l.to_array() == [1, 2, 3]
