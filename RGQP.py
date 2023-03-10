
import f_x_p

def RGQP(s, t, b, beta, x, counter, graph):

    path = []
    if graph[s, t] > b:
        return []
    if s == t:
        path = [s]
    else:
        path = [s, t]
    if counter == 0:
        return path
    m = f_x_p.f_x_p(x, path, beta)

    for v in se:
        B_1 = 1

        se.remove(v)

        while B_1 < B:
            print('[RGQP]current B_1 is ', B_1)
            P_1 = RGQP(s, v, B_1, Beta, X, se, counter-1, graph)

            P_2 = RGQP(v, t, B - B_1, Beta, X + P_1, se, counter - 1, graph)

            if f_x_p.f_x_p(X, P_1 + P_2, Beta) > m:
                P0 = P_1 + P_2
                m = f_x_p.f_x_p(X, P0, Beta)

                P = list(set(P0))
                P.sort(key=P0.index)

            B_1 += 10

    print('[RGQP]RGQP is finished.')
    return P