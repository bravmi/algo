class Matrix:
    def __init__(self, data=None):
        if data is None:
            data = []
        self._matrix = [row[:] for row in data]
        if self:
            assert len({len(row) for row in self}) == 1

    def __str__(self) -> str:
        lines = []
        lines.append('[')
        lines.extend(f'    {str(row)},' for row in self)
        lines.append(']')
        return '\n'.join(lines)

    def __repr__(self) -> str:
        return repr(self._matrix)

    def inverse(self, method='cramer') -> 'Matrix':
        n, m = self.shape
        if n != m:
            raise ValueError('cannot invert non-square matrix')

        if method == 'cramer':
            return self.cramer()
        else:
            raise ValueError('unknown inverse method')

    def cramer(self) -> 'Matrix':
        A = self
        n = len(A)

        if n == 1:
            x = A[0][0]
            if not x:
                raise ValueError('singular matrix')
            return Matrix([[1 / x]])
        det = self.det()
        if not det:
            raise ValueError('singular matrix')
        if n == 2:
            return Matrix(
                [
                    [A[1][1] / det, -1 * A[0][1] / det],
                    [-1 * A[1][0] / det, A[0][0] / det],
                ]
            )

        C = Matrix()  # cofactors
        for i in range(n):
            row = []
            for j in range(n):
                row.append((-1) ** (i + j) * A.minor(i, j).det())
            C.append(row)

        # inverse
        B = C.transpose()
        for i in range(n):
            for j in range(n):
                B[i][j] /= det
        return B

    def copy(self) -> 'Matrix':
        return Matrix(self._matrix)

    def transpose(self, inplace=False) -> 'Matrix':
        A = self if inplace else self.copy()
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A

    def minor(self, i: int, j: int) -> 'Matrix':
        return Matrix([row[:j] + row[j + 1 :] for row in (self[:i] + self[i + 1 :])])

    def det(self) -> float:
        A = self
        n, m = self.shape
        if n != m:
            raise ValueError('cannot calculate determinant of non-square matrix')

        if n == 0:
            raise ValueError('matrix cannot be empty')
        elif n == 1:
            return A[0][0]
        elif n == 2:
            return A[0][0] * A[1][1] - A[0][1] * A[1][0]

        det = 0
        for j in range(n):
            if A[0][j]:
                M = A.minor(0, j)
                det += (-1) ** j * A[0][j] * M.det()
        return det

    def __len__(self) -> int:
        return len(self._matrix)

    def __getitem__(self, index: int | slice) -> list:
        if isinstance(index, slice):
            return [row[:] for row in self._matrix[index]]
        return self._matrix[index]

    def __setitem__(self, index: int | slice, value) -> None:
        self._matrix[index] = value

    def append(self, row: list) -> None:
        self._matrix.append(row)
        if self:
            assert len({len(row) for row in self}) == 1

    def insert(self, index, row) -> None:
        self._matrix.insert(index, row)

    def __iter__(self):
        yield from self._matrix

    def __mul__(self, other) -> 'Matrix':
        A, B = self, other
        n = A.shape[0]
        m = B.shape[1]

        C = Matrix([[None] * m for _ in range(n)])

        for i, a in enumerate(A):
            for j, b in enumerate(zip(*B)):
                C[i][j] = sum(x * y for x, y in zip(a, b))
        return C

    def __eq__(self, other) -> bool:
        return self._matrix == other._matrix

    @property
    def shape(self) -> tuple:
        A = self._matrix
        return len(A), len(A[0]) if A else 0

    def allclose(self, other, atol=1e-8) -> bool:
        if self.shape != other.shape:
            return False

        A, B = self, other
        n, m = A.shape
        return all(abs(A[i][j] - B[i][j]) <= atol for i in range(n) for j in range(m))

    def __add__(self, other) -> 'Matrix':
        A, B = self, other
        n, m = A.shape
        C = Matrix([[None] * m for _ in range(n)])

        for i in range(n):
            for j in range(m):
                C[i][j] = A[i][j] + B[i][j]
        return C

    def __iadd__(self, other) -> 'Matrix':
        A, B = self, other
        n, m = A.shape

        for i in range(n):
            for j in range(m):
                A[i][j] += B[i][j]
        return A

    def __sub__(self, other) -> 'Matrix':
        A, B = self, other
        n, m = A.shape
        C = Matrix([[None] * m for _ in range(n)])

        for i in range(n):
            for j in range(m):
                C[i][j] = A[i][j] - B[i][j]
        return C

    def __isub__(self, other) -> 'Matrix':
        A, B = self, other
        n, m = A.shape

        for i in range(n):
            for j in range(m):
                A[i][j] -= B[i][j]
        return A

    def tolist(self) -> list:
        return [row[:] for row in self]


def zeros(n: int, m: int | None = None) -> 'Matrix':
    m = m or n
    mat = [[0 for j in range(m)] for i in range(n)]
    return Matrix(mat)


def eye(n: int) -> 'Matrix':
    mat = zeros(n)
    for i in range(n):
        mat[i][i] = 1
    return Matrix(mat)


if __name__ == '__main__':
    A = [
        [3 / 2, 1, 1 / 2],
        [1, 2, 1],
        [1 / 2, 1, 3 / 2],
    ]
    A = Matrix(A)  # type: ignore
    B = [
        [1 / 2, 0],
        [0, 0],
        [0, 1 / 2],
    ]
    B = Matrix(B)  # type: ignore
    C = [
        [3 / 4, 1 / 4],
        [1 / 2, 1 / 2],
        [1 / 4, 3 / 4],
    ]
    C = Matrix(C)  # type: ignore

    assert A * B == C  # type: ignore
