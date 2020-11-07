import itertools as it
from typing import Any, Optional

from ..utils import nextprime, random_string

NHASH = 1009
MULTIPLER = 31
NGROW = 2
NLIMIT = 1


class Hash:
    def __init__(
        self, iterable=None, nhash=NHASH, multipler=MULTIPLER, nlimit=NLIMIT
    ) -> None:
        self._nhash = nhash
        self._multiplier = multipler
        self._nlimit = nlimit
        self._symtab: list = [[] for _ in range(self._nhash)]
        self._running_average = 0  # list length average

        if iterable:
            self.extend(iterable)

    def extend(self, iterable) -> None:
        for k, v in iterable:
            self[k] = v

    @classmethod
    def fromkeys(
        cls, iterable, value=None, nhash=NHASH, multipler=MULTIPLER
    ) -> 'Hash':
        items = ((k, value) for k in iterable)
        return cls(iterable=items, nhash=nhash, multipler=multipler)

    def __getitem__(self, key):
        h = self._hash(key)
        for k, v in self._symtab[h]:
            if k == key:
                return v
        raise KeyError

    def __setitem__(self, key, value) -> None:
        h = self._hash(key)
        row = self._symtab[h]
        for index, (k, _) in enumerate(row):
            if k == key:
                row[index] = (key, value)
                return

        row.append((key, value))
        self._running_average += 1 / self._nhash
        if self._running_average >= self._nlimit:
            self._grow()

    def get(self, key, default=None):
        h = self._hash(key)
        for k, v in self._symtab[h]:
            if k == key:
                return v
        return default

    def _grow(self) -> None:
        items = list(self.items())
        nhash = nextprime(self._nhash * NGROW)
        self.__init__(items, nhash=nhash)  # type: ignore

    def __contains__(self, key) -> bool:
        h = self._hash(key)
        return any(k == key for k, _ in self._symtab[h])

    def __iter__(self):
        for k, _ in self.items():
            yield k

    def items(self):
        for row in self._symtab:
            for k, v in row:
                yield k, v

    def _hash(self, key) -> int:
        s = str(key)
        h = 0
        for c in s:
            h = self._multiplier * h + ord(c)
        return h % self._nhash

    def find_collision(self, key: Any) -> Optional[str]:
        """just a way to find a collision"""
        for i in it.count(0):
            key2: str = str(key) + chr(i)
            if self._hash(key2) == self._hash(key):
                return key2
        return None

    def collisions(self) -> dict:
        return {h: row for h, row in enumerate(self._symtab) if len(row) > 1}

    def average_length(self) -> int:
        return (
            sum(len(row) for _, row in enumerate(self._symtab)) / self._nhash
        )

    def to_dict(self) -> dict:
        return {h: row for h, row in enumerate(self._symtab) if row}

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return repr(self.to_dict())


if __name__ == '__main__':
    nhash = 100
    h = Hash(nhash=nhash)
    for i in range(nhash - 1):
        k = random_string(6)
        h[k] = True
    print(len(h))
