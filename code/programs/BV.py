from qiskit import (
    # IBMQ,
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer,
)


def dec2bin(n):
    a = 1
    list = []
    while a > 0:
        a, b = divmod(n, 2)
        list.append(str(b))
        n = a
    s = ""
    for i in range(len(list) - 1, -1, -1):
        s += str(list[i])
    s = s.zfill(10)
    return s


def inverse(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '0':
            s_list[i] = '1'
        else:
            s_list[i] = '0'
    s = "".join(s_list)
    return s


def BV(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(10)
    register = QuantumRegister(10)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    circuit_drawer(qc, filename='./BV_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(10)
    register = QuantumRegister(10)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(oracle[i])

    qc.cnot(oracle[6], oracle[0])  # M4

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    circuit_drawer(qc, filename='./BV_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(10)
    register = QuantumRegister(10)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(oracle[i])

    qc.swap(oracle[6], oracle[0])  # M2

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    circuit_drawer(qc, filename='./BV_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(10)
    register = QuantumRegister(10)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(oracle[i])

    qc.ccx(oracle[5], oracle[6], oracle[0])  # M3

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    circuit_drawer(qc, filename='./BV_M3_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(10)
    register = QuantumRegister(10)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.cnot(register[6], register[0])  # M4
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    circuit_drawer(qc, filename='./BV_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(10)
    register = QuantumRegister(10)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.cswap(register[5], register[8], register[0])  # M5
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    circuit_drawer(qc, filename='./BV_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    oracle = QuantumRegister(10)
    register = QuantumRegister(10)
    qc = QuantumCircuit(oracle, register)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    # from qiskit.tools.visualization import circuit_drawer
    #
    # circuit_drawer(qc, filename='./BV_circuit')

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = BV_specification(input)
    for i in range(1024):
        temp = 0
        for j in range(1024):
            temp += abs(t[i * 1024 + j]) ** 2
        pt.append(temp)
    return pt
