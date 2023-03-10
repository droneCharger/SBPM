
import sbpm.f_x_p
def rg(starting, ending, b, beta_new, x, counter, graph,gamma,phi):

    M1 = 100000
    path = []

    if graph[starting, ending] > b:
        return path

    if starting == ending:
        path = [starting]
    else:
        path = [starting, ending]

    if counter == 0:
        return path

    m = sbpm.f_x_p.f_x_p(x, path, beta_new, gamma, phi, graph)

    b_1 = 1
    for i in range(len(graph)):
        if graph[i, 0] < M1:
            while b_1 <= b:

                path_1 = rg(starting, i, b_1, beta_new, x, counter - 1, graph)
                if len(path_1) ==0:
                    b_1 = b+1
                    break

                if isinstance(x, list):
                    xlist = x
                else:
                    xlist = list(map(int, str(x)))

                xpath = xlist+path_1
                xpath = [i for n, i in enumerate(xpath) if i not in xpath[:n]]

                path_2 = rg(i, ending, b - b_1, beta_new, xpath, counter - 1, graph)
                if len(path_2) ==0:
                    b_1 = b+1
                    break

                if sbpm.f_x_p.f_x_p(x, path_1 + path_2, beta_new) > m:
                    path_0 = path_1 + path_2
                    m = sbpm.f_x_p.f_x_p(x, path_0, beta_new)

                    path = path_0

                b_1 += 1
    return path