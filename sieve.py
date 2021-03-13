"""
From here:
https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
"""

import itertools as it


def sieve(n: int):
    pass


def sieve_gen():
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes."""
    D = {}  # map each composite integer to its first-found prime factor
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


def tests():
    first_10 = list(it.islice(sieve_gen(), 0, 10))
    assert first_10 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


if __name__ == '__main__':
    tests()
