import sbpm.powersetsbinary1
import sbpm.comput_length

def dis_shortest(s_00, s_dd, sub, graph):
    all_sub = sbpm.powersetsbinary1.powersetsbinary1(sub)

    result_length = 10000
    result_path = []

    nn = len(all_sub)
    i = 0

    while i < nn:

        tp = all_sub[i]

        pt = [s_00] + tp + [s_dd]

        len_temp = sbpm.comput_length.comput_length(pt, graph)

        i = i + 1
        if len_temp < result_length:
            result_length = len_temp
            result_path = tp
    return result_path, result_length