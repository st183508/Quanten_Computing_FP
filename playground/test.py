import quanten_computing_fp as qc
from qiskit import QuantumCircuit

hello_str = qc.hello()


def greet(name: str) -> str:
    return "Hello, " + name


qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)

"""
print(greet("Einstein"))


A = [np.array([[1, 2], [3, 4]]), np.array([[1, 5], [4, 3]]), np.array([[2, 1], [6, 7]])]

print(qc.matrix_product(A))
A = [qc.pauli_x(), qc.pauli_y(), qc.pauli_z()]
print(qc.matrix_sum(A))

print(qc.matrix_power(qc.pauli_y(), 3))
"""
