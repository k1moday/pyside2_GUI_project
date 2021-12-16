from numpy import *
import numpy as np


def bayesianChain(data, Lx0):
    # function[muak, sigmaak] = BayesianChain(data, Lx0)
    mua0 = Lx0[0]
    sigmaa0 = Lx0[1]
    sigmaB = Lx0[2]
    b = Lx0[3]
    m = np.size(data, 0)
    musave = []
    sigmasave = []

    for i in range(1, m):  # 运行时间
        mu_basic_up = 0
        mu_basic_low = 0
        sigma_basic = 0
        for j in range(1, i):
            tim_0 = data[j - 1, 0]
            tim_1 = data[j, 0]
            X_0 = data[j - 1, 1]
            X_1 = data[j, 1]
            mu_basic_up = mu_basic_up + (X_1 - X_0) * (tim_1 ** b - tim_0 ** b) / sigmaB ** 2 / (tim_1 - tim_0)
            mu_basic_low = mu_basic_low + (tim_1 ** b - tim_0 ** b) / sigmaB ** 2 / (tim_1 - tim_0)
            sigma_basic = sigma_basic + (tim_1 ** b - tim_0 ** b) / sigmaB ** 2 / (tim_1 - tim_0)
        mu_up = mu_basic_up + mua0 / sigmaa0 ** 2
        mu_low = mu_basic_low + 1 / sigmaa0 ** 2

        mu_now = mu_up / mu_low
        sigma_now = (1 / (sigma_basic + 1 / sigmaa0 ** 2)) ** 0.5

        musave = np.append(musave, mu_now)
        sigmasave = np.append(sigmasave, sigma_now)

    muak = musave
    sigmaak = sigmasave
    return muak, sigmaak
