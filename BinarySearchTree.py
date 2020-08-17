import collections as co
import random
from typing import Deque, Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value}'


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, curr, value) -> Node:
        if curr is None:
            return Node(value)

        if value <= curr.value:
            curr.left = self._insert(curr.left, value)
        elif value > curr.value:
            curr.right = self._insert(curr.right, value)
        return curr

    def lookup(self, value) -> Optional[Node]:
        return self._lookup(self.root, value)

    def _lookup(self, curr, value) -> Optional[Node]:
        if curr is None:
            return None

        if value == curr.value:
            return curr
        elif value < curr.value:
            return self._lookup(curr.left, value)
        elif value > curr.value:
            return self._lookup(curr.right, value)
        return None

    def preorder(self) -> list:
        acc: list = []
        self._preorder(self.root, acc)
        return acc

    def _preorder(self, curr, acc: list) -> None:
        if curr is None:
            return

        acc.append(curr.value)
        if curr.left:
            self._preorder(curr.left, acc)
        if curr.right:
            self._preorder(curr.right, acc)

    def postorder(self) -> list:
        acc: list = []
        self._postorder(self.root, acc)
        return acc

    def _postorder(self, curr, acc: list) -> None:
        if curr is None:
            return

        if curr.left:
            self._postorder(curr.left, acc)
        if curr.right:
            self._postorder(curr.right, acc)
        acc.append(curr.value)

    def inorder(self) -> list:
        acc: list = []
        self._inorder(self.root, acc)
        return acc

    def _inorder(self, curr, acc: list) -> None:
        if curr is None:
            return

        if curr.left:
            self._inorder(curr.left, acc)
        acc.append(curr.value)
        if curr.right:
            self._inorder(curr.right, acc)

    def level_order(self) -> list:
        if self.root is None:
            return []

        acc = []
        queue: Deque = co.deque([self.root])
        while queue:
            node = queue.pop()
            if node is None:
                continue
            acc.append(node.value)
            queue.appendleft(node.left)
            queue.appendleft(node.right)
        return acc

    def validate(self) -> bool:
        values = self.inorder()
        return all(x < y for x, y in zip(values, values[1:]))

    def extend(self, values) -> None:
        for x in values:
            self.insert(x)


def sort(values) -> list:
    tree = BinarySearchTree()
    tree.extend(values)
    return tree.inorder()


def test1():
    node1 = Node(1)
    node3 = Node(3)
    node2 = Node(2, node1, node3)

    node5 = Node(5)
    node7 = Node(7)
    node6 = Node(6, node5, node7)
    node4 = Node(4, node2, node6)
    tree = BinarySearchTree(node4)

    assert tree.lookup(1).value == 1
    assert tree.lookup(2).value == 2
    assert tree.lookup(3).value == 3
    assert tree.lookup(1000) is None

    assert tree.preorder() == [4, 2, 1, 3, 6, 5, 7]
    assert tree.postorder() == [1, 3, 2, 5, 7, 6, 4]
    assert tree.inorder() == [1, 2, 3, 4, 5, 6, 7]
    assert tree.level_order() == [4, 2, 6, 1, 3, 5, 7]
    assert tree.validate()


def test2():
    a = [random.randrange(0, 10) for _ in range(10)]
    assert sort(a) == sorted(a)


if __name__ == '__main__':
    a = [random.randrange(0, 10) for _ in range(10)]
    tree = BinarySearchTree()
    tree.extend(a)
    assert tree.inorder() == sorted(a)
