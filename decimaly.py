def decimal(n: int, d: int, prec=100):
    if n * d < 0:
        yield '-'
    n = abs(n)
    d = abs(d)

    q, r = divmod(n, d)
    yield str(q)
    if not r:
        return

    yield '.'
    for _ in range(prec):
        r *= 10
        q, r = divmod(r, d)
        yield str(q)
        if not r:
            return


def tests():
    assert ''.join(decimal(1, 14, 17)) == '0.07142857142857142'


if __name__ == '__main__':
    pass
