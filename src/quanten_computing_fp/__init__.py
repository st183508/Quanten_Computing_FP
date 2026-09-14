import numpy as np


def hello() -> str:
    return "Hello from quanten-computing-fp!"


def pauli_x():
    return np.array([[0, 1], [1, 0]])


def pauli_y():
    return np.array([[0, -1j], [1j, 0]])


def pauli_z():
    return np.array([[1, 0], [0, -1]])


def matrix_sum(A):
    for i in range(len(A) - 1):
        matrix_sum_var = A[i] + A[i + 1]

    return matrix_sum_var
