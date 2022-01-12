import random
import math
from scipy.integrate import quad
from matplotlib import pyplot as plt
from sympy import integrate, symbols
from BayesianChain import bayesianChain
import numpy as np

X0 = 0

mua = 1
sigmaa = 0.02
b = 1.5
tao = symbols('tao')


def mu(tao):
    return random.normalvariate(mua, sigmaa) * b * tao ** (b - 1)


def Fmu(t):
    v, err = quad(mu, 0, t)
    return v


sigmaB = 0.2


def X(t):
    return X0 + Fmu(t) + sigmaB * random.normalvariate(0, t)


X_save = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
omiga = 25  # 退化阈值
minX = 0  # 退化量最小值存储器
delta_t = 0.01  # 采样时间间隔
tim = 0.01  # 总时间
while minX < omiga:
    temp1 = X(tim)
    temp2 = X(tim)
    temp3 = X(tim)
    temp4 = X(tim)
    temp5 = X(tim)
    temp6 = X(tim)
    temp7 = X(tim)

    tempRow = np.array([tim, temp1, temp2, temp3, temp4, temp5, temp6, temp7])
    X_save = np.vstack((X_save, tempRow))
    minX = min([temp1, temp2, temp3, temp4, temp5, temp6, temp7])
    tim = tim + delta_t

x = X_save[:, 0]
y1 = X_save[:, 1]
y2 = omiga

Tmax = np.empty((1, 1), dtype=float)
for i in range(1, 8):
    X_temp = X_save[:, i]
    tempIdx = 0
    for index in range(len(X_temp)):
        if X_temp[index] <= 25:
            tempIdx = index
        else:
            break;

    Tmax = np.append(Tmax, X_save[tempIdx, 0])

x = len(Tmax)
y = Tmax
curX = np.empty((0, 1), dtype=int)
for index in range(len(y)):
    curX = np.append(curX, index + 1)


def F(mua0, sigmaa0, sigmaB0, b0):
    L = 1
    for j in range(0, 7):
        # for j = 1:7
        T = Tmax[j]
        L_temp = 1 / (2 * math.pi * T ** 3 * (sigmaa0 ** 2 * T ** (2 * b0 - 1) + sigmaB0 ** 2)) ** 0.5 * \
                 (omiga - (T ** b0 - b0 * T ** b0) * (omiga * sigmaa0 ** 2 * T ** (b0 - 1) + mua0 * sigmaB0 ** 2) /
                  (sigmaa0 ** 2 * T ** (2 * b0 - 1) + sigmaB0 ** 2)) * \
                 math.exp(-(omiga - mua0 * T ** b0) ** 2 / (2 * T * (sigmaa0 ** 2. * T ** (2 * b0 - 1) + sigmaB0 ** 2)))
        L = L * L_temp
    return L


emf = 10 ** 4

Fsave = np.array([[0.0, 0.0]])
jud = 0
temp = 0
randjud = 0.999
N = 20
Lx0 = [1, 0.02, 0.2, 1.5]
while jud < 10:
    temp1 = F(Lx0[0], Lx0[1], Lx0[2], Lx0[3])
    count = 0

    STEP = 1
    jud1 = 0
    Fsaved = np.zeros((N, 5))
    while temp <= temp1 and jud1 < randjud:
        #           randX = (rand(1, 4) - 0.5) * STEP;
        #           Lx1 = Lx0 + randX;
        for k in range(0, N):
            randX = (np.random.rand(1, 4) - 0.5) * STEP
            Lx1 = Lx0 + randX
            for index in range(len(Lx1)):
                Lx1[index] = np.round(Lx1[index] * 10 ** 7) / 10 ** 7
                if Lx1[0, 1] <= 0 or Lx1[0, 2] <= 0:
                    k = k - 1
                else:
                    temp = np.append(F(Lx1[0, 0], Lx1[0, 1], Lx1[0, 2], Lx1[0, 3]), Lx1)
                    Fsaved[k, :] = temp

        Fsavedmax = -1
        for index in range(len(Fsaved[:, 0])):
            if Fsaved[index, 0] > Fsavedmax:
                idx = index
                Fsavedmax = Fsaved[index, 0]
        Lx1 = np.double(Fsaved[idx, 1:5])
        temp = Fsavedmax

        #           jud1 = rand;
        count = count + 1
        check = count % 2
        #        check = rem(count, 2)

        if check >= 1:
            STEP = STEP / 2

    epsA = Lx0 - Lx1
    eps = round(np.linalg.norm(epsA), 4)
    #        eps = vpa(norm(epsA), 4)
    Lx0 = Lx1
    #    Fsave = [Fsave;FF(Lx1), eps]
    Fsave = np.append(Fsave, [[F(Lx1[0], Lx1[1], Lx1[2], Lx1[3]), eps]], axis=0)

    if eps < 10 ** (-5):
        jud = jud + 1
    else:
        jud = 0

up = len(Fsave)

Lxinit = Lx1


def mu_1(tao):
    return random.normalvariate(Lxinit[0], Lxinit[1]) * Lxinit[3] * tao ** (Lxinit[3] - 1)


def X_1(t):
    v, err = quad(mu_1, 0, t) + Lxinit[2] * random.normalvariate(0, 1)
    return v


X_UP = 0
tim = delta_t
X_save = np.array([[0.0, 0.0]])
while X_UP < omiga:
    X_UP = X_1(tim)
    X_save = np.vstack((X_save, [tim, X_UP]))
    tim = tim + delta_t

tim_first = tim - delta_t

x = X_save[:, 0]
y1 = X_save[:, 1]
y2 = omiga
plt.plot(x, y1, 'k-')
plt.hlines(y2, 0, 9, color="blue")
plt.show()

[muak, sigmaak] = bayesianChain(X_save, Lxinit)
time = X_save[:, 0]
time = np.delete(time, 0, 0)

# x = time
# y = muak
# plt.plot(x, y, 'r-')
# plt.xlabel("退化时间")
# plt.ylabel("μ数值")
# plt.show()
#
# x = time
# y = sigmaak
# plt.plot(x, y, 'b-')
# plt.xlabel("退化时间")
# plt.ylabel("σ数值")
# plt.show()
