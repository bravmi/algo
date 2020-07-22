import random
import pytest


def square_check(x: int, m: int) -> int:
    """Miller-Rabin"""
    r = (x * x) % m
    if r == 1 and x not in [1, m - 1]:
        return 0
    else:
        return r


def expmod(base: int, exp: int, m: int) -> int:
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        x = expmod(base, exp // 2, m)
        return square_check(x, m)
    else:
        return (base * expmod(base, exp - 1, m)) % m


def fermat_test(n: int) -> bool:
    a = random.randrange(1, n)
    return expmod(a, n - 1, n) == 1


def fast_prime(n: int, times: int) -> bool:
    return all(fermat_test(n) for _ in range(times))


def prime(n: int) -> bool:
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    return fast_prime(n, 10)


@pytest.mark.slow
def test():
    import sympy as sp

    it = (n for n in range(2, 10000) if prime(n) != sp.isprime(n))
    assert next(it, None) is None


if __name__ == '__main__':
    import sympy as sp

    it = (n for n in range(2, 10000) if prime(n) != sp.isprime(n))
    print(next(it, None))
