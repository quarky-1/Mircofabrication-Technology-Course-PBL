import numpy as np

def evaporation_rate(T, P):
    return (T / (P + 1e-5)) * 1e-3