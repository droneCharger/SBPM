
import numpy as np
import sbpm.comput_length
import sbpm.dis_shortest
import sbpm.algorithm2
import sbpm.compute_passengers
import sbpm.satisfy_capacity
import sbpm.find_min_deadline
import sbpm.satisfy_length_constraint
def cop(graph,nn,all_sub,s_0,s_00,s_d,s_dd,delta,delta_1,beta,passengers,
        capacity,deadlines,speed, t1_max,t2_max,number_passengers,gamma,phi):
    final_less_pathset = []
    final_equal_pathset = []
    number_less = 0
    number_equal = 0
    social_welfare_less = 0
    social_welfare_less_path = []
    social_welfare_equal = 0
    social_welfare_equal_path = []
    counter = 0
    M1 = 100000
    while counter < nn:
        pathi = all_sub.loc[[counter],:]
        pathi = pathi.dropna(axis=1,how='any')
        tpathi0 = np.array(pathi.iloc[0])
        tpathi0 = tpathi0.tolist()
        tpathi0 = list(map(int, tpathi0[:]))
        tpathi = []

        for it in range(len(tpathi0)):
            if graph[tpathi0[it],0] < M1:
                tpathi.append(tpathi0[it])

        counter = counter + 1

        if len(tpathi) < delta_1:
            sum_beta_re_path = 0

            re_path, re_length = sbpm.dis_shortest.dis_shortest(s_00, s_dd, tpathi, graph)

            final_less_pathset.append(re_path)

            number_less += 1
            for i in re_path:
                sum_beta_re_path += beta[i]
            social_welfare_temp =sum_beta_re_path - re_length * gamma * phi
            if social_welfare_less < social_welfare_temp:
                social_welfare_less =social_welfare_temp
                social_welfare_less_path = [s_00] + re_path + [s_dd]
        elif len(tpathi) == delta_1:
            sum_eq_path = 0
            path_equal = sbpm.algorithm2.algorithm2\
                (s_00, s_dd, tpathi,beta,graph,delta,passengers, capacity,
                 deadlines,speed, t1_max,t2_max,number_passengers,gamma,phi)
            equal_path = [s_00] + path_equal + [s_dd]

            equal_path_length = sbpm.comput_length.comput_length(equal_path,graph)
            for i in path_equal:
                sum_eq_path += beta[i]
            social_welfare_temp_ = sum_eq_path - equal_path_length * gamma * phi
            if social_welfare_equal < social_welfare_temp_:
                social_welfare_equal =social_welfare_temp_
                social_welfare_equal_path = equal_path
    if social_welfare_less < social_welfare_equal:
        social_welfare_final_path = social_welfare_equal
        final_path = social_welfare_equal_path

    else:
        social_welfare_final_path = social_welfare_less
        final_path = social_welfare_less_path

    path_capacity = sbpm.compute_passengers.compute_passengers(final_path,passengers)
    final_path_length = sbpm.comput_length.comput_length(final_path, graph)
    if path_capacity > capacity:

        final_path = sbpm.satisfy_capacity.satisfy_capacity(final_path,capacity,passengers)
    path_capacity = sbpm.compute_passengers.compute_passengers(final_path, passengers)
    min_deadline = sbpm.find_min_deadline.find_min_deadline(final_path, deadlines)
    path_length_constraint = \
        speed * (min_deadline- path_capacity * (t1_max + t2_max))

    if final_path_length > path_length_constraint:

        final_path = sbpm.satisfy_length_constraint.satisfy_length_constraint(final_path,deadlines,t1_max,t2_max,speed,graph,passengers)
    sum_beta_final_path = 0
    for i in final_path:
        sum_beta_final_path += beta[i]
    final_path_length = sbpm.comput_length.comput_length(final_path, graph)
    social_welfare_final_path = sum_beta_final_path - final_path_length * gamma * phi
    return social_welfare_final_path,final_path