from typing import Optional


class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_

    def __str__(self) -> str:
        return f'{self.value}'


class List:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, value) -> None:
        self.head = Node(value, self.head)

    def append(self, value) -> None:
        if not self:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def extend(self, iterable) -> None:
        for x in iterable:
            self.prepend(x)
        self.reverse()

    def nodes(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def get_tail(self) -> Optional[Node]:
        if not self:
            return None

        node = self.head
        while node.next:
            node = node.next
        return node

    def find(self, value) -> Node:  # type: ignore
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        if node is None:
            raise ValueError

    def __contains__(self, value) -> bool:
        return any(x == value for x in self)

    def remove(self, value) -> None:
        prev = None
        curr = self.head
        while curr:
            if curr.value == value:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        raise ValueError

    def reversed(self) -> 'List':
        new_list = List()
        for value in self:
            new_list.prepend(value)
        return new_list

    def reverse(self) -> None:
        return self.reverse_iter()

    def reverse_iter(self) -> None:
        if not self.head or not self.head.next:
            return

        prev = None
        curr = self.head
        while curr:
            # curr.next, prev, curr = prev, curr, curr.next
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_
        self.head = prev

    def copy(self) -> 'List':
        new_list = List()
        for x in self:
            new_list.prepend(x)
        new_list.reverse()
        return new_list

    def merge(self, other) -> 'List':
        return self + other

    def __add__(self, other) -> 'List':
        new_list = List()
        for x in self:
            new_list.prepend(x)
        for x in other:
            new_list.prepend(x)
        new_list.reverse()
        return new_list

    def __iadd__(self, other) -> 'List':
        if not self:
            self.head = other.head
            return self

        node = self.head
        while node.next:
            node = node.next
        node.next = other.head
        return self

    def __getitem__(self, index: int):
        n = len(self)
        if index < 0:
            index += n
        if not (0 <= index < n):
            raise IndexError

        node = self.head
        for _ in range(index):
            node = node.next
        return node.value

    def __setitem__(self, index: int, value):
        n = len(self)
        if index < 0:
            index += n
        if not (0 <= index < n):
            raise IndexError

        node = self.head
        for _ in range(index):
            node = node.next
        node.value = value

    def clear(self) -> None:
        prev = None
        curr = self.head
        self.head = None
        while curr:
            prev = curr
            curr = curr.next
            prev.next = None

    def __bool__(self) -> bool:
        return self.head is not None

    def __len__(self) -> int:
        return sum(1 for x in self)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return '[{}]'.format(', '.join(repr(x) for x in self))

    def to_array(self) -> list:
        return [x for x in self]

    def apply(self, func) -> None:
        for x in self:
            func(x)

    def insert_before(self, x, y) -> None:
        """insert y value before x value"""
        prev = None
        curr = self.head
        while curr and curr.value != x:
            prev, curr = curr, curr.next
        if curr is None:
            raise ValueError

        xnode = curr
        ynode = Node(y)
        if prev is None:
            ynode.next = xnode
            self.head = ynode
        else:
            prev.next, ynode.next = ynode, xnode

    def insert_after(self, x, y) -> None:
        """insert y value after x value"""
        xnode = self.find(x)
        ynode = Node(y)
        xnode.next, ynode.next = ynode, xnode.next


if __name__ == '__main__':
    l = List()
    l.extend([1, 2, 3])
    print(l[0])
