import math

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


def CE(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_M1(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])

    qc.cnot(b[6], b[0])  # M1
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    # circuit_drawer(qc, filename='./CE_M2_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_M2(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])

    qc.swap(b[6], b[0])  # M2
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    # circuit_drawer(qc, filename='./CE_M2_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_M3(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])

    qc.cswap(b[5], b[8], b[0])  # M3

    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    # circuit_drawer(qc, filename='./CE_M3_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_M4(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])

    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.x(b[0])  # M4
    qc.measure(b, c)

    # circuit_drawer(qc, filename='./CE_M4_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_M5(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])

    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.h(b[0])  # M5

    qc.measure(b, c)

    # circuit_drawer(qc, filename='./CE_M5_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    qc = QuantumCircuit(a, b)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = CE_specification(input)
    for i in range(2048):
        temp = 0
        for j in range(8):
            temp += abs(t[i * 8 + j]) ** 2
        pt.append(temp)
    return pt
