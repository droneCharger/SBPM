
def powersetsbinary1(items):

    all_sub = []
    cc = 0

    N = len(items)
    for i in range(2 ** N):

        zj = []
        for j in range(N):

            if (i >> j) % 2 == 1:

                zj.append(items[j])
        if len(zj) == N:

            all_sub.append(zj)
            #print('[powersetbinary1] all_sub ', all_sub)
            cc = cc +1
    return all_sub