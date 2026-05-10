import numpy as np

def cvd_rate(T):
    Ea = 0.5
    k = 8.617e-5
    return np.exp(-Ea / (k * T))