import pytest

from .matrix import *


def test_transpose():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = [
        [1, 3],
        [2, 4],
    ]
    B = Matrix(B)

    assert A.transpose() == B


def test_transpose_inplace():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = [
        [1, 3],
        [2, 4],
    ]
    B = Matrix(B)

    A.transpose(inplace=True)
    assert A == B


def test_mul():
    A = [
        [3 / 2, 1, 1 / 2],
        [1, 2, 1],
        [1 / 2, 1, 3 / 2],
    ]
    A = Matrix(A)
    B = [
        [1 / 2, 0],
        [0, 0],
        [0, 1 / 2],
    ]
    B = Matrix(B)
    C = [
        [3 / 4, 1 / 4],
        [1 / 2, 1 / 2],
        [1 / 4, 3 / 4],
    ]
    C = Matrix(C)

    assert A * B == C


def test_sub():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = A.copy()
    C = [
        [0, 0],
        [0, 0],
    ]
    C = Matrix(C)

    assert A - B == C


def test_isub():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = A.copy()
    C = [
        [0, 0],
        [0, 0],
    ]
    C = Matrix(C)

    A -= B
    assert A == C


def test_add():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = A.copy()
    C = [
        [2, 4],
        [6, 8],
    ]
    C = Matrix(C)

    assert A + B == C


def test_iadd():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = A.copy()
    C = [
        [2, 4],
        [6, 8],
    ]
    C = Matrix(C)

    A += B
    assert A == C


def test_det():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)

    assert A.det() == -2


def test_inverse3():
    A = [
        [1, -1 / 2, 0],
        [-1 / 2, 1, -1 / 2],
        [0, -1 / 2, 1],
    ]
    A = Matrix(A)
    B = [
        [3 / 2, 1, 1 / 2],
        [1, 2, 1],
        [1 / 2, 1, 3 / 2],
    ]
    B = Matrix(B)

    assert A.inverse() == B


def test_inverse_non_square():
    A = [[1, 2]]
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.inverse()


def test_inverse_zero1():
    A = [[0]]
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.inverse()


def test_inverse_zero2():
    A = [
        [0, 0],
        [0, 0],
    ]
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.inverse()


def test_inverse_zero3():
    A = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.inverse()


def test_str():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)

    assert str(A) == "[\n    [1, 2],\n    [3, 4],\n]"


def test_repr():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)

    assert repr(A) == "[[1, 2], [3, 4]]"


def test_inverse1():
    A = [[1]]
    A = Matrix(A)
    B = A.copy()

    assert A.inverse() == B


def test_inverse2():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = [
        [-2, 1],
        [1.5, -0.5],
    ]
    B = Matrix(B)

    assert A.inverse() == B


def test_det_none():
    A = [[]]
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.det()


def test_det_non_square():
    A = [
        [1, 2],
    ]
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.det()


def test_det_no_rows():
    A = []
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.det()


def test_det1():
    A = [[1]]
    A = Matrix(A)

    assert A.det() == 1


def test_det4():
    A = [
        [0, 4, 3, 3],
        [6, 8, 0, 4],
        [9, 6, 8, 4],
        [3, 7, 7, 0],
    ]
    A = Matrix(A)

    assert A.det() == 1560


def test_setitem_int():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)

    A[1] = [5, 6]
    assert A[1] == [5, 6]


def test_setitem_slice():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    A = Matrix(A)
    B = [
        [0, 0, 0],
        [0, 0, 0],
        [7, 8, 9],
    ]
    B = Matrix(B)

    A[0:2] = [[0, 0, 0], [0, 0, 0]]
    assert A == B


def test_getitem_slice():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    A = Matrix(A)
    B = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    B = Matrix(B)

    assert Matrix(A[0:2]) == B


def test_insert():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)

    A.insert(1, [5, 6])
    assert A[1] == [5, 6]


def test_allclose():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = [[x + 1e-9 for x in row] for row in A]
    B = Matrix(B)

    assert not A == B
    assert A.allclose(B)


def test_allclose_different_shapes():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)
    B = [[1, 2]]
    B = Matrix(B)

    assert not A.allclose(B)


def test_inverse_unknown():
    A = [
        [1, 2],
        [3, 4],
    ]
    A = Matrix(A)

    with pytest.raises(ValueError):
        A.inverse(method='unknown')


def test_zeros():
    A = zeros(2)
    B = [
        [0, 0],
        [0, 0],
    ]

    assert A.tolist() == B


def test_eye():
    A = eye(2)
    B = [
        [1, 0],
        [0, 1],
    ]

    assert A.tolist() == B
