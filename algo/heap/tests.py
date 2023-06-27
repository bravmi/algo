from .heap import Heap


def test_push_and_pop():
    h = Heap()

    # Test push and root
    h.push(3)
    assert h.root() == 3
    h.push(2)
    assert h.root() == 2
    h.push(15)
    assert h.root() == 2
    h.push(5)
    assert h.root() == 2
    h.push(4)
    assert h.root() == 2
    h.push(45)
    assert h.root() == 2

    # Test pop
    assert h.pop() == 2
    assert h.root() == 3
    assert h.pop() == 3
    assert h.root() == 4
    assert h.pop() == 4
    assert h.root() == 5
    assert h.pop() == 5
    assert h.root() == 15
    assert h.pop() == 15
    assert h.root() == 45
    assert h.pop() == 45

    # Test heap is empty
    assert str(h) == '[]'


def test_heapify():
    h = Heap([3, 2, 15, 5, 4, 45])
    assert h.root() == 2
    assert h.values() == [2, 3, 15, 5, 4, 45]


def test_push_pop():
    # Test empty heap
    h = Heap()
    assert h.push_pop(5) == 5

    # Test heap with one element
    h = Heap([2])
    assert h.push_pop(3) == 2
    assert h.values() == [3]

    # Test heap with multiple elements
    h = Heap([3, 2, 6, 8, 7])
    assert h.push_pop(1) == 1
    assert h.values() == [2, 3, 6, 8, 7]

    # Test heap where new value is greater than root
    h = Heap([3, 2, 6, 8, 7])
    assert h.push_pop(4) == 2
    assert h.values() == [3, 4, 6, 8, 7]

    # Test heap where new value is less than root
    h = Heap([3, 2, 6, 8, 7])
    assert h.push_pop(1) == 1
    assert h.values() == [2, 3, 6, 8, 7]


def test_max_heap():
    values = [3, 2, 15, 5, 4, 45]
    h = Heap([-x for x in values])
    assert -h.root() == 45
    assert [-x for x in h.values()] == [45, 5, 15, 2, 4, 3]
