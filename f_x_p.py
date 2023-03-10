
import sbpm.comput_length
def f_x_p(x, path, beta, gamma, phi, graph):

    q = path + [x]
    q = [i for n, i in enumerate(q) if i not in q[:n]]
    sum_q1 = 0
    for i in range(len(q)):
        sum_q1 += beta[i]
    sum_q = sum_q1 - gamma * phi * sbpm.comput_length.comput_length(q,graph)

    sum_x1 = 0
    if len([x]) == 0:
        sum_x = 0
    else:
        for i in range(len([x])):
            sum_x1 += beta[i]
        x = [i for n, i in enumerate(x) if i not in x[:n]]
        sum_x = sum_x1 - gamma * phi * comput_length.comput_length(x,graph)

    return sum_q - sum_x