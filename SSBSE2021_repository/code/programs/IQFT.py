import numpy as np
from qiskit import (
    #IBMQ,
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer,
)
from math import pi
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import circuit_drawer
from rpy2 import robjects as robjects

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
    s = s.zfill(10)#input的位数
    return s

def inverse(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '0':
            s_list[i] = '1'
        else:
            s_list[i] ='0'
    s = "".join(s_list)
    return s

def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft_rotations(circuit, qubit, p):
    """Performs qft on the first n qubits in circuit (without swaps)"""
    # if n == 0:
    #     return circuit
    # n -= 1
    # circuit.h(9-n)
    # for qubit in range(n):
    #     circuit.cu1(pi/2**(n-qubit), qubit, n)
    # # At the end of our function, we call the same function again on
    # # the next qubits (we reduced n by one earlier in the function)
    # qft_rotations(circuit, n)

    # for qubit in range(n):
    #     circuit.h(qubit)
    #     p = 1
    #     for j in range(qubit + 1, 10):
    #         circuit.cu1(pi/2**(p), qubit, j)
    #         p += 1
    #     circuit.barrier()
    # return circuit

    # for qubit in range(n):
    #     circuit.h(qubit)
    #     p = 1
    for j in range(qubit + 1, 10):
        circuit.cu1(pi/2**(p), qubit, j)
        p += 1
    circuit.barrier()
    return circuit

def IQFT(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc,10)
    #qft_rotations(qc,10)
    for qubit in range(10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.barrier()

    qc.measure(q,c)

    #circuit_drawer(qc, filename='./IQFT_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])

    qc.barrier()

    qc.ch(q[3],q[4])#M1

    swap_registers(qc,10)
    #qft_rotations(qc,10)
    for qubit in range(10):
        qc.h(qubit)
        qft_rotations(qc,qubit,1)

    qc.barrier()

    qc.measure(q,c)

    #circuit_drawer(qc, filename='./IQFT_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc,10)
    for qubit in range(3):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)
    qc.ch(q[4],q[2])#M2
    for qubit in range(3,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.barrier()

    qc.measure(q,c)

    #circuit_drawer(qc, filename='./IQFT_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def IQFT_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(3):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.ch(q[4],q[3])#M3
    qft_rotations(qc,3,1)
    for qubit in range(4,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M3_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    qc.ch(q[2], q[4])#M4

    swap_registers(qc, 10)
    for qubit in range(10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.ch(q[8],q[3])#M5

    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts



def IQFT_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc,10)
    #qft_rotations(qc,10)
    for qubit in range(10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.barrier()

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = IQFT_specification(input)
    for i in range(1024):
        pt.append(abs(t[i])**2)
    return pt



if __name__ == '__main__':
    # print(probabilityComputing(16))
    # print(probabilityComputing_M2(16))
    # print(probabilityComputing_M3(16))
    f = open("iqft_M3_test.txt","a")
    for i in range(1023):
        f.write('--------------------')
        f.write('\n')
        f.write(str(i))
        f.write(str(probabilityComputing_M3(i)))
        f.write('\n')
    f.close()
    # print(QRAM(0,2))
    # print(QRAM_M1(0, 2))
    # print(QRAM_M2(0, 2))
    # print(QRAM_M3(0, 2))
    # print(QRAM_M4(0, 2))
    # print(QRAM_M5(0, 2))
    #print(probabilityComputing(104))
    #IQFT(0,1024)
    #print(IQFT_M(8,1024))
    # print(IQFT(0,1024))
    # print(IQFT_M1(0,1024))
    # print(IQFT_M2(0, 1024))
    #print(IQFT_M3(0, 1024))
    # print(IQFT_M4(0, 1024))
    # print(IQFT_M5(0, 1024))



    # temp = IQFT_M1(200,1024)
    # print(temp)
    # fre = []
    # p = probabilityComputing(8)
    # print(p)
    # for i in range(1024):
    #     j_s = dec2bin(i)
    #     if j_s in temp:
    #         fre.append(temp[j_s])
    #     else:
    #         fre.append(0)
    # fre = np.array(fre)
    # p = np.array(p)
    # fre = robjects.FloatVector(fre)
    # p = robjects.FloatVector(p)
    # print(fre)
    # print(p)
    # robjects.r('''
    #        chitest<-function(observed,theoretical){
    #            test_result <- chisq.test(x = observed,p = theoretical)
    #            pvalue = test_result$p.value
    #            return (pvalue)
    #        }
    # ''')
    # t = robjects.r['chitest'](fre,p)
    # pvalue = t[0]
    # print(pvalue)





    # a = probabilityComputing(8)
    # for i in range(1024):
    #     print(a[i])
    # print(sum(a))
    # AmplitudeAmplification(3,1)
    # AmplitudeAmplification_M1(3,1)
    # AmplitudeAmplification_M2(3,1)
    # AmplitudeAmplification_M3(3,1)
    # AmplitudeAmplification_M4(3,1)
    # AmplitudeAmplification_M5(3,1)
    # AmplitudeAmplification_M6(3,1)
    # # # f = open('./specification.txt','a')
    # f1 = open('./counts.txt','a')
    # a = probabilityComputing(400)
    # # for i in range(len(a)):
    # #     f.write(str(a[i]))
    # #     f.write('\n')
    # temp = AmplitudeAmplification(400,1)
    # for i in range(len(a)):
    #     i_s = dec2bin(i)
    #     if i_s not in temp:
    #         fre.append(0)
    #     else:
    #         fre.append(temp[i_s])
    #     f1.write(str(fre[i]))
    #     f1.write('\n')
