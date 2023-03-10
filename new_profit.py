def new_profit(graph_up, beta, passengers, delta_star,i_k):

    M1 = 100000
    beta_new = [0] * len(beta)
    for i in range(len(graph_up)):
        if graph_up[i, 1] < M1 and passengers[i] > 0:
            if beta[i] / passengers[i] < (1+delta_star)**i_k:
                beta_new[i] = 0
            else:
                beta_new[i] = beta[i]
    return beta_new