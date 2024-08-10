import string
import base64
from . import itertools_
import pytest

CHARS = '{}{}{}{}'.format(
    string.ascii_uppercase,
    string.ascii_lowercase,
    string.digits,
    '+/',
).encode()


def encode(b: bytes) -> bytes:
    bits = ''.join(f'{byte:08b}' for byte in b)
    groups = [''.join(g) for g in itertools_.grouper(bits, 6, fillvalue='0')]
    result = bytes(CHARS[int(g, 2)] for g in groups)
    padding = b'=' * (-len(result) % 4)  # why max two =?
    return result + padding


def decode(b: bytes) -> bytes:
    indexes = [CHARS.index(byte) for byte in b.rstrip(b'=')]
    bits = ''.join(f'{i:06b}' for i in indexes)
    groups = [''.join(g) for g in itertools_.grouper(bits, 8, incomplete='ignore')]
    result = b''.join(int(g, 2).to_bytes() for g in groups)
    return result


@pytest.mark.parametrize(
    'test_input, expected',
    [
        (b'hello world', b'aGVsbG8gd29ybGQ='),
        (b'', b''),
        (b'hel', b'aGVs'),
    ],
)
def test_encode(test_input: bytes, expected: bytes):
    assert encode(test_input) == base64.b64encode(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    [
        (b'aGVsbG8gd29ybGQ=', b'hello world'),
        (b'', b''),
        (b'aGVs', b'hel'),
    ],
)
def test_decode(test_input: bytes, expected: bytes):
    assert decode(test_input) == base64.b64decode(test_input) == expected


if __name__ == '__main__':
    b = b'hello world'
    for i in range(len(b)):
        print(b[:i], encode(b[:i]), base64.b64encode(b[:i]))
        encoded = encode(b[:i])
