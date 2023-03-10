def find_x(starting,ending,graph_up):
    M1 = 100000
    xx = ending
    for i in range(len(graph_up)):
        if graph_up[i, 0] < M1 and i != starting and i != ending:
            xx = i
    return xx