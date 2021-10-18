import itertools as it

import pytest

from ..utils import random_string
from .hash import Hash


def test_basic():
    h = Hash([('joe', 1), ('bob', 2), ('sam', 3)])
    assert 'joe' in h
    assert h['joe'] == 1
    h['joe'] = 0
    assert h['joe'] == 0
    assert h['sam'] == 3
    h['sam'] = 4
    assert h['sam'] == 4
    assert h.get('sam') == 4
    assert len(h) == 3
    assert h._running_average == pytest.approx(h.average_length())

    assert h.get('beth') is None
    with pytest.raises(KeyError):
        h['beth']
    h.extend([('don', 7), ('greg', 8)])
    assert len(h) == 5

    assert str(h) == str(h.to_dict())


def test_collision():
    items = set([('joe', 1), ('bob', 2), ('sam', 3), ('joeϏ', 4)])
    h = Hash(items)
    assert set(h.items()) == items
    assert len(h.collisions()[h._hash('joe')]) == 2


def test_collisions_100():
    n = 10
    h = Hash.fromkeys(('d' * i for i in range(n)), nhash=100)
    # chr(100) = 'd', so perfect collision at 0
    assert len(h._symtab[0]) == n
    assert sum(1 for row in h._symtab if row)


def test_collisions_search():
    s = 'aaa'
    h = Hash()
    h_value = h._hash(s)
    gen = (s + chr(i) for i in it.count(0) if h._hash(s + chr(i)) == h_value)
    assert next(gen) == 'aaa' == h.find_collision(s)
    assert next(gen) == 'aaa҃'
    assert next(gen) == 'aaaࡴ'
    assert next(gen) == 'aaa౥'


def test_grow():
    nhash = 100
    h = Hash(nhash=nhash)
    for i in range(nhash - 1):
        k = random_string(6)
        h[k] = True
    running_average = h._running_average
    assert running_average == pytest.approx(1, abs=0.01)
    h[random_string(6)] = True
    h[random_string(6)] = True
    assert h._running_average < running_average
    assert h._nhash > nhash


def test_str_int():
    h = Hash([(5, 1), ('5', 2)])
    assert len(h.to_dict()) == 1
    assert len(h) == 2


if __name__ == '__main__':
    pass
