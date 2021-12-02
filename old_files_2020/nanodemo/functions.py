import numpy as np


def linear(x, m, c):
    return m * x + c

def hertz(x, a1, b1, cp, k, bead_radius):

    def fitfunc_hertz(x, a1, b1, cp, k, bead_radius):
        if x <= cp:
            return a1 + b1 * x
        elif x > cp:
            return (4 / 3) * k * ((x - cp) ** (3 / 2)) * np.sqrt(bead_radius)

    y = np.zeros(x.shape)
    for i in range(len(y)):
        y[i] = fitfunc_hertz(x[i], a1, b1, cp, k, bead_radius)
    return y
