
import pandas as pd
import sbpm.cop
import sbpm.construct_graph
import sbpm.belong
def main_sbpm(k_b,number_data,delta,delta_1,capacity,s_0,s_00,s_d,s_dd,df,speed,passengers, beta, deadlines,number_passengers):

    q = 1
    M1 = 100000
    gamma = 0.15

    phi = 0.64

    graph_lat = df['lat'][0:number_data]
    graph_long = df['long'][0:number_data]

    graph0 = sbpm.construct_graph.construct_graph(graph_lat, graph_long, number_data)


    subsetpath = 'D:\mta\data\subset\subset_' + str(number_data) + '.csv'

    all_sub = pd.read_csv(subsetpath, names=['0', '1', '2', '3', '4'])

    nn = all_sub.iloc[:, 0].size

    t1_max, t2_max = 0.008, 0.008

    winner_set = []
    social_welfare_set = []
    graph = graph0
    while q <= k_b:
        social_welfare_final_q = 0
        final_q_path=[]
        for i in range(number_data):
            social_welfare_final_path,final_path = \
                sbpm.cop.cop(graph,nn,all_sub,s_0,s_00,s_d,s_dd,delta,delta_1,beta,passengers,
                        capacity,deadlines,speed, t1_max,t2_max,number_passengers,gamma,phi)

            if social_welfare_final_q < social_welfare_final_path:
                final_q_path = final_path
                social_welfare_final_q = social_welfare_final_path

        i2 = 1
        while i2 < len(final_q_path):
            graph[final_q_path[i2],0] = M1
            i2 = i2 +1

        if (final_q_path in winner_set) == False:
            winner_set.append(final_q_path)
            social_welfare_set.append(social_welfare_final_q)
        q = q + 1

    rho = [0] * number_data
    sw_diff = [0] * number_data

    for stop in range(number_data):
        graph1 = sbpm.construct_graph.construct_graph(graph_lat, graph_long, number_data)
        flag = sbpm.belong.belong(stop, winner_set)
        rho_temp = 0
        if stop != s_00 and stop != s_dd and flag==1:
            graph1[stop,0] = M1
            for ilist in winner_set:
                if len(ilist) > 0:
                    winner_pay_set = []
                    social_welfare_pay_set = []
                    q_ = 1
                    while q_ <= k_b:
                        social_welfare_final_q_ = 0
                        final_q_path_ = []
                        for i in range(number_data):
                            social_welfare_final_path_, final_path_ = \
                                sbpm.cop.cop(graph1, nn, all_sub, s_0, s_00, s_d, s_dd, delta, delta_1, beta, passengers,
                                capacity, deadlines, speed, t1_max, t2_max, number_passengers, gamma, phi)
                            if social_welfare_final_q_ < social_welfare_final_path_:
                                final_q_path_ = final_path_
                                social_welfare_final_q_ = social_welfare_final_path_

                        i2 = 1
                        while i2 < len(final_q_path_):
                            graph1[final_q_path_[i2], 0] = M1
                            i2 = i2 + 1
                        winner_pay_set.append(final_q_path_)
                        social_welfare_pay_set.append(social_welfare_final_q_)
                        q_ = q_ + 1

                    sw_winner = 0
                    sw_payment = 0
                    for i_1 in social_welfare_set:
                        sw_winner = sw_winner + i_1
                    for i_2 in social_welfare_pay_set:
                        sw_payment =sw_payment + i_2
                    sw_diff = sw_payment - sw_winner
                    rho_temp = rho_temp + max(0, sw_diff + beta[stop])

        rho[stop] = rho_temp

    total_social_welfare = 0
    for i3 in social_welfare_set:
        total_social_welfare = total_social_welfare + i3

    total_rho = 0
    for i4 in rho:
        total_rho = total_rho + i4

    number_winner = 0
    print('[main_sbpm]winner_set=',winner_set)
    for i5 in winner_set:
        number_winner = number_winner + len(i5)
    return total_social_welfare,total_rho,number_winner