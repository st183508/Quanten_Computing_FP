import quanten_computing_fp as qc

hello_str = qc.hello()


def greet(name: str) -> str:
    return "Hello, " + name


print(greet("Einstein"))

A = [qc.pauli_x(), qc.pauli_y(), qc.pauli_z()]
print(qc.matrix_sum(A))
