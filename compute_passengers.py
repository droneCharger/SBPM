
def compute_passengers(path, passengers):

    number = 0
    for i in path:
        number = number + passengers[i]
    return number