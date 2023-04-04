import itertools as it
import random
import string

from .miller_rabin import isprime


def nextprime(n: int) -> int:
    """
    >>> nextprime(0)
    2
    >>> nextprime(1000)
    1009
    """
    return next(x for x in it.count(n + 1) if isprime(x))


def random_string(n: int, upper=False) -> str:
    items = string.ascii_lowercase + string.digits
    if upper:
        items += string.ascii_uppercase
    return ''.join(random.choice(items) for _ in range(n))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
