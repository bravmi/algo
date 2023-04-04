class Bits:
    def __init__(self, number: int):
        self._number = number

    def set_bit(self, index: int) -> 'Bits':
        mask = 1 << index
        self._number |= mask
        return self

    def get_bit(self, index: int) -> int:
        mask = 1 << index
        return 1 if self._number & mask else 0

    def clear_bit(self, index) -> 'Bits':
        mask = ~(1 << index)
        self._number &= mask
        return self

    def clear_bits_msb_to_index(self, index: int) -> 'Bits':
        mask = (1 << index) - 1
        self._number &= mask
        return self

    def clear_bits_index_to_lsb(self, index: int) -> 'Bits':
        mask = ~((1 << index + 1) - 1)
        self._number &= mask
        return self

    def twos_complement(self, num_bits: int) -> str:
        if not self._fits(num_bits):
            raise ValueError('not enough bits for the number')

        if self._number >= 0:
            return bin(self._number)[2:].zfill(num_bits)
        else:
            return bin(self._number + 2**num_bits)[2:].zfill(num_bits)

    def _fits(self, num_bits: int) -> bool:
        return -(2**num_bits) <= self._number <= (2**num_bits - 1)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        num_bits = 0
        while not self._fits(num_bits):
            num_bits += 1
        num_bits += 1
        return self.twos_complement(num_bits)


def test_get_bit():
    b = Bits(10)
    bits = '01010'
    for i, c in enumerate(reversed(bits)):
        assert b.get_bit(i) == int(c)


def test_clear():
    n = int('10001110', base=2)
    b = Bits(n)
    assert str(b.clear_bit(3)) == '010000110'
    b = Bits(n)
    assert str(b.clear_bits_msb_to_index(3)) == '0110'
    b = Bits(n)
    assert str(b.clear_bits_index_to_lsb(3)) == '010000000'


def test_twos_complement():
    b = Bits(10)
    assert str(b) == '01010'
    b = Bits(-5)
    assert str(b) == '1011'
    b = Bits(127)
    assert str(b) == '01111111'
    b = Bits(-128)
    assert str(b) == '10000000'


if __name__ == '__main__':
    b = Bits(127)
    print(b)
