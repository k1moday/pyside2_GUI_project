import numpy as np
from combine import combineAct
import copy

A1 = np.array([[1, 2, -2, 2, 3, 0],
               [2, 3, -1, 4, 5, 6],
               [3, 0, 0, 0, 0, 0],
               [4, 0, 0, 0, 0, 0],
               [5, 2, -2, 7, 8, 0],
               [6, 0, 0, 0, 0, 0],
               [7, 0, 0, 0, 0, 0],
               [8, 0, 0, 0, 0, 0]])

mOriginal = len(A1)
nOriginal = len(A1[0])

m = len(A1)
n = len(A1[0])

strs = []
for i in range(0, mOriginal):
    strs.append('s[' + str(A1[i][0]) + ']')

while m != 1:
    [A2, strsChanged] = combineAct(A1, strs)
    A1 = A2
    strs = strsChanged
    m = len(A1)
    n = len(A1[0])

lam = [0.001, 0.005, 0.004, 0.003, 0.002]
baseEvent = [3, 7, 8, 6, 4]

x = 100
trial = 1000000


def monteCarlo(lam_, strsChanged_, baseEvent_, x_, trial_, n_):
    failureVector = [0 for q in range(len(baseEvent_))]
    # topEvent = []
    countTopEventTrue = 0
    countBaseEventTrue = [0 for q in range(len(baseEvent_))]
    for i in range(trial_):
        monteC = []
        s = [0 for q in range(n_ + 1)]
        for j in range(len(baseEvent_)):
            monteC.append(np.random.exponential(1 / lam_[j]))
            if monteC[j] <= x_:
                failureVector[j] = 1
                countBaseEventTrue[j] += 1
            else:
                failureVector[j] = 0
            s[baseEvent_[j] - 1] = failureVector[j]

        countTopEventTrue += eval(strsChanged_[0])

    topPro = countTopEventTrue / trial_

    return topPro


topPro1 = monteCarlo(lam, strsChanged, baseEvent, x, trial, mOriginal)

delta = 0.1
lamOrigin = copy.deepcopy(lam)

for i in range(len(baseEvent)):
    lam[i] = lamOrigin[i] * (1 + delta)

topPro2 = monteCarlo(lam, strsChanged, baseEvent, x, trial, mOriginal)

nodeImportance = [0.0 for n in range(len(baseEvent))]
for i in range(len(baseEvent)):
    nodeImportance[i] = (topPro2 - topPro1) / (-np.exp(-lam[i] * x) + np.exp(-lamOrigin[i] * x))

print(nodeImportance)

