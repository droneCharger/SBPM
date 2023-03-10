
def max_ratio(graph_up, beta, passengers):

    M1 = 100000
    max_re = 0
    for i in range(len(graph_up)):
        if graph_up[i,1] < M1:
            ratio = beta[i] / passengers[i]

            if max_re < ratio:
                max_re = ratio
    return max_re