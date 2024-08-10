"""
Taken from here:
https://docs.python.org/3/library/itertools.html#itertools-recipes
"""
import itertools
import typing


def grouper(
    iterable: typing.Iterable[typing.Any],
    n: int,
    *,
    incomplete: str = 'fill',
    fillvalue: typing.Any | None = None,
) -> typing.Iterator[tuple[typing.Any, ...]]:
    "Collect data into non-overlapping fixed-length chunks or blocks."
    # grouper('ABCDEFG', 3, fillvalue='x') → ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') → ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') → ABC DEF
    iterators = [iter(iterable)] * n
    match incomplete:
        case 'fill':
            return itertools.zip_longest(*iterators, fillvalue=fillvalue)
        case 'strict':
            return zip(*iterators, strict=True)
        case 'ignore':
            return zip(*iterators)
        case _:
            raise ValueError('Expected fill, strict, or ignore')
