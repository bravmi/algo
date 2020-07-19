import string

DIGITS = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return DIGITS[0]
    else:
        sign = 1

    x *= sign
    digits = []
    while x:
        q, r = divmod(x, base)
        digits.append(DIGITS[r])
        x = q
    if sign < 0:
        digits.append('-')
    digits.reverse()

    return ''.join(digits)


def test1():
    assert int2base(100, 2) == '1100100' == f'{100:b}'
    assert int2base(100, 16) == '64' == f'{100:x}'
    assert int2base(100, 8) == '144' == f'{100:o}'
    assert int2base(-100, 8) == '-144' == f'{-100:o}'
    assert int2base(0, 8) == '0' == f'{0:o}'
    assert int2base(100, 10) == '100'


if __name__ == '__main__':
    print(int2base(27, 16))
