import numpy as np


def combineAct(A1, strs):
    m = len(A1)
    n = len(A1[0])
    temp = 0
    for i in range(m):
        nodeSon = A1[i, 3:n]
        nodeSon = nodeSon.tolist()
        while 0 in nodeSon:
            nodeSon.remove(0)
        j = 0
        for j in range(len(nodeSon)):
            k = A1[:, 0].tolist().index(nodeSon[j])
            if A1[k][1] != 0:
                break

        if j == len(nodeSon) - 1:
            temp = i
            break

    strsChanged = strs
    strsChanged[temp] = '(' + strsChanged[nodeSon[0] - 1]
    for i in range(len(nodeSon) - 1):
        if A1[temp][2] == -1:
            strsChanged[temp] = strsChanged[temp] + '&' + strsChanged[nodeSon[i]]
        if A1[temp][2] == -2:
            strsChanged[temp] = strsChanged[temp] + '|' + strsChanged[nodeSon[i]]

    strsChanged[temp] = strsChanged[temp] + ')'

    A1[temp, 1:n] = 0

    for i in range(len(nodeSon)):
        k = A1[:, 0].tolist().index(nodeSon[i])
        A1 = np.delete(A1, k, axis=0)

    return [A1, strsChanged]
