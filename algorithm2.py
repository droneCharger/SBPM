import sbpm.preprocess
import sbpm.max_ratio
import math
import sbpm.new_profit
import sbpm.compute_passengers
import sbpm.satisfy_capacity
import sbpm.compute_profile
import sbpm.rg
import sbpm.find_x


def algorithm2(s_00, s_dd, path,beta,graph,delta,passengers, capacity,
               deadlines,speed, t1_max,t2_max,number_passengers,gamma,phi):
    M1 = 100000
    graph_up = sbpm.preprocess.preprocess(path,passengers,graph)
    delta_star =  delta/(1-delta)

    max_rt = sbpm.max_ratio.max_ratio(graph_up, beta, passengers)


    path_uncap = [s_00, s_dd]
    path_cap = []
    i_k = k

    while len(path_cap) == 0 and i_k >= 0:
        beta_new = sbpm.new_profit.new_profit(graph_up, beta, passengers, delta_star, i_k)
        for i in range(len(graph_up)):
            if graph_up[i,0] < M1:
                starting = i
            else:
                break
                for j in range(len(graph_up)):
                    if graph_up[j, 0] < M1:
                        ending = j
                        b = (deadlines[i] - passengers[j] * (t1_max+t2_max))* speed - graph[s_00,starting] - graph[ending,s_dd]

                        x = sbpm.find_x.find_x(starting,ending,graph_up)

                        counter = 500
                        sbpm.rg.rg(starting, ending, b, beta_new, x, counter, graph_up,gamma, phi)

                    else:
                        break
        passengers_path = sbpm.compute_passengers.compute_passengers(path, passengers)

        if passengers_path <= capacity:
            path_uncap = [s_00] + path + [s_dd]
        else:
            path_cap = path

        i_k = i_k - 1

    path_cap_cap = sbpm.satisfy_capacity.satisfy_capacity(path_cap, capacity,passengers)

    profile_path_uncap = sbpm.compute_profile.compute_profile(path_uncap,beta_new)
    profile_path_cap_cap = sbpm.compute_profile.compute_profile(path_cap_cap,beta_new)
    if profile_path_uncap > profile_path_cap_cap:
        return path_uncap
    else:
        return path_cap_cap