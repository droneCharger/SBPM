
def preprocess(path,passengers,graph):
    min_r = 10000
    M1 = 100000
    for i in range(len(path)):
        if min_r > passengers[path[i]]:
            min_r = passengers[path[i]]

    nn = len(graph)
    for i in range(nn):
        if passengers[i] > min_r and not (i in path):
            graph[i,0] = M1
    return graph