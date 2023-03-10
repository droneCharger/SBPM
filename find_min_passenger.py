
def  find_min_passenger(path_cap,passengers):
    min_pas_index = 0
    min_pas = 1000
    for i in range(len(path_cap)):
        if min_pas <passengers[path_cap[i]]:
            min_pas = passengers[path_cap[i]]
            min_pas_index = i
    return min_pas_index