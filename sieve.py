"""
From here:
https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
"""
import itertools as it
from typing import Iterator


def sieve(n: int) -> list[int]:
    """Returns  a list of primes < n"""
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def sieve_gen() -> Iterator[int]:
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes."""
    # map each composite integer to its first-found prime factor
    D: dict[int, int] = {}
    yield 2
    for q in it.count(3, step=2):  # q gets 2, 3, 4, 5, ... ad infinitum
        p = D.pop(q, None)
        if p is None:
            # mark q squared as not-prime (with q as first-found prime factor)
            D[q * q] = q
            # q not a key in D, so q is prime, therefore, yield it
            yield q
        else:
            # let x <- smallest q+(n*p) which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = q + p
            while x in D or not (x & 1):
                x += p
            D[x] = p


def test_sieve_gen():
    n = 10
    first_n = list(it.islice(sieve_gen(), 0, n))
    assert first_n == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sieve():
    assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def tests():
    n = 100
    first_n = list(it.islice(sieve_gen(), 0, n))
    assert sieve(first_n[-1] + 1) == first_n


if __name__ == '__main__':
    tests()
