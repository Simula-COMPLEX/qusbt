import collections

import numpy as np
import rpy2.robjects as robjects

from programs import DM, AI, CE, AS, SM, BV, QRAM, IQFT


def dec2bin(n, dec2bin_param):
    a = 1
    list = []
    while a > 0:
        a, b = divmod(n, 2)
        list.append(str(b))
        n = a
    s = ""
    for i in range(len(list) - 1, -1, -1):
        s += str(list[i])
    s = s.zfill(dec2bin_param)
    return s


def wrong_output(i, right_output):
    set_output = set(right_output)
    if i not in set_output:
        return True  # existing wrong output
    return False


def ReadTxtName(rootdir):
    lines = []
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    return lines


def Unique(input, i):
    counts = collections.Counter(input)
    if counts[input[i]] == 1:
        return True
    else:
        return False


def calculate_fail_number_GA(input, dec2bin_param, group_name, program_name, algorithm):
    count_fail = 0  # the number that fails the test
    count_wrong = []  # number of wrong output
    pvalue = []
    global f

    f = open('./result/' + group_name + '/' + program_name + '_' + algorithm + '.txt', 'a')
    print(str(input) + ' ' + str(len(input)))
    for i in range(len(input)):  # fix
        flag_wrong = False  # have wrong outputs
        fre = []  # counts of expected outputs
        p = []  # possibility of expected outputs
        wrong = 0  # number of wrong outputs
        count_times = 0
        right_output = []

        # calculate specification
        ##
        pt = get_pv(program_name, i, input)
        ##

        for j in range(len(pt)):
            if pt[j] > 1e-4:  # threshold
                count_times += 1
                right_output.append(j)
                p.append(pt[j])

        # calculate outputs

        ##
        temp = get_counts(program_name, group_name, count_times, i, input)
        ##

        # judge wrong outputs
        for j in range(len(pt)):
            # j_s = dec2bin(j)
            j_s = dec2bin(j, dec2bin_param)
            if j_s in temp:
                if wrong_output(j, right_output):
                    flag_wrong = True
                    wrong += temp[j_s]
        count_wrong.append(wrong)

        # chi test
        if flag_wrong == False:  # no wrong output
            if count_times == 1:  # only one output
                pvalue.append(1)
            else:
                for j in range(len(p)):
                    # j_s = dec2bin(right_output[j])
                    j_s = dec2bin(right_output[j], dec2bin_param)
                    if j_s in temp:
                        fre.append(temp[j_s])
                    else:
                        fre.append(0)
                p = np.array(p)
                fre = np.array(fre)
                p = robjects.FloatVector(p)
                fre = robjects.FloatVector(fre)
                robjects.r('''
                    chitest<-function(observed,theoretical){
                        test_result <- chisq.test(x = observed,p = theoretical)
                        pvalue = test_result$p.value
                        return (pvalue)
                    }
             ''')
                t = robjects.r['chitest'](fre, p)
                pvalue.append(t[0])
        else:
            pvalue.append(0)

        if pvalue[i] < 0.01 and Unique(input, i):
            count_fail += 1

    count_fail = [count_fail]
    count_fail = np.array(count_fail)

    ###write in file
    for i in range(len(input)):
        f.write(str(input[i]))
        f.write(' ')
    f.write('\n')
    for i in range(len(input)):
        f.write(str(count_wrong[i]))
        f.write(' ')
    f.write('\n')
    for i in range(len(input)):
        f.write(str(pvalue[i]))
        f.write(' ')
    f.write('\n')
    f.write(str(count_fail[0]))
    f.write('\n')

    print(count_fail)
    return count_fail


def get_counts(program_name, group_name, count_times, i, input):
    if program_name == 'AI':
        if group_name == 'AI_1':
            return AI.AI_M1(int(input[i]), count_times)  # getting counts
        elif group_name == 'AI_2':
            return AI.AI_M2(int(input[i]), count_times)  # getting counts
        elif group_name == 'AI_3':
            return AI.AI_M3(int(input[i]), count_times)  # getting counts
        elif group_name == 'AI_4':
            return AI.AI_M4(int(input[i]), count_times)  # getting counts
        elif group_name == 'AI_5':
            return AI.AI_M5(int(input[i]), count_times)  # getting counts
        else:
            return None
    elif program_name == 'BV':
        if group_name == 'BV_1':
            return BV.BV_M1(int(input[i]), count_times)  # getting counts
        elif group_name == 'BV_2':
            return BV.BV_M2(int(input[i]), count_times)  # getting counts
        elif group_name == 'BV_3':
            return BV.BV_M3(int(input[i]), count_times)  # getting counts
        elif group_name == 'BV_4':
            return BV.BV_M4(int(input[i]), count_times)  # getting counts
        elif group_name == 'BV_5':
            return BV.BV_M5(int(input[i]), count_times)  # getting counts
        else:
            return None
    elif program_name == 'CE':
        if group_name == 'CE_1':
            return CE.CE_M1(int(input[i]), count_times)  # getting counts
        elif group_name == 'CE_2':
            return CE.CE_M2(int(input[i]), count_times)  # getting counts
        elif group_name == 'CE_3':
            return CE.CE_M3(int(input[i]), count_times)  # getting counts
        elif group_name == 'CE_4':
            return CE.CE_M4(int(input[i]), count_times)  # getting counts
        elif group_name == 'CE_5':
            return CE.CE_M5(int(input[i]), count_times)  # getting counts
        else:
            return None
    elif program_name == 'DM':
        if group_name == 'DM_1':
            return DM.DM_M1(int(input[i]), count_times)  # getting counts
        elif group_name == 'DM_2':
            return DM.DM_M2(int(input[i]), count_times)  # getting counts
        elif group_name == 'DM_3':
            return DM.DM_M3(int(input[i]), count_times)  # getting counts
        elif group_name == 'DM_4':
            return DM.DM_M4(int(input[i]), count_times)  # getting counts
        elif group_name == 'DM_5':
            return DM.DM_M5(int(input[i]), count_times)  # getting counts
        else:
            return None
    elif program_name == 'SM':
        if group_name == 'SM_1':
            return SM.SM_M1(int(input[i]), count_times)  # getting counts
        elif group_name == 'SM_2':
            return SM.SM_M2(int(input[i]), count_times)  # getting counts
        elif group_name == 'SM_3':
            return SM.SM_M3(int(input[i]), count_times)  # getting counts
        elif group_name == 'SM_4':
            return SM.SM_M4(int(input[i]), count_times)  # getting counts
        elif group_name == 'SM_5':
            return SM.SM_M5(int(input[i]), count_times)  # getting counts
        else:
            return None
    elif program_name == 'AS':
        if group_name == 'AS_1':
            return AS.AS_M1(int(input[i]), count_times)  # getting counts
        elif group_name == 'AS_2':
            return AS.AS_M2(int(input[i]), count_times)  # getting counts
        elif group_name == 'AS_3':
            return AS.AS_M3(int(input[i]), count_times)  # getting counts
        elif group_name == 'AS_4':
            return AS.AS_M4(int(input[i]), count_times)  # getting counts
        elif group_name == 'AS_5':
            return AS.AS_M5(int(input[i]), count_times)  # getting counts
        else:
            return None
    elif program_name == 'QRAM':
        if group_name == 'QRAM_1':
            return QRAM.QRAM_M1(int(input[i], count_times))
        elif group_name == 'QRAM_2':
            return QRAM.QRAM_M2(int(input[i], count_times))
        elif group_name == 'QRAM_3':
            return QRAM.QRAM_M3(int(input[i], count_times))
        elif group_name == 'QRAM_4':
            return QRAM.QRAM_M4(int(input[i], count_times))
        elif group_name == 'QRAM_5':
            return QRAM.QRAM_M5(int(input[i], count_times))
        else:
            return None
    elif program_name == 'IQFT':
        if group_name == 'IQFT_1':
            return IQFT.IQFT_M1(int(input[i], count_times))
        elif group_name == 'IQFT_2':
            return IQFT.IQFT_M2(int(input[i], count_times))
        elif group_name == 'IQFT_3':
            return IQFT.IQFT_M3(int(input[i], count_times))
        elif group_name == 'IQFT_4':
            return IQFT.IQFT_M4(int(input[i], count_times))
        elif group_name == 'IQFT_5':
            return IQFT.IQFT_M5(int(input[i], count_times))
        else:
            return None


def get_pv(program_name, i, input):
    if program_name == 'AI':
        return AI.probabilityComputing(int(input[i]))  # getting probability
    elif program_name == 'BV':
        return BV.probabilityComputing(int(input[i]))  # getting probability
    elif program_name == 'CE':
        return CE.probabilityComputing(int(input[i]))  # getting probability
    elif program_name == 'DM':
        return DM.probabilityComputing(int(input[i]))  # getting probability
    elif program_name == 'SM':
        return SM.probabilityComputing(int(input[i]))  # getting probability
    elif program_name == 'AS':
        return AS.probabilityComputing(int(input[i]))  # getting probability
    elif program_name == 'QRAM':
        return QRAM.probabilityComputing(int(input[i]))  # getting probability
    elif program_name == 'IQFT':
        return IQFT.probabilityComputing(int(input[i]))  # getting probability
    else:
        return None
