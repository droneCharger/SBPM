
def compute_profile(path,beta_new):
    profile = 0
    for i in range(len(path)):
        profile = profile + beta_new[path[i]]
    return profile