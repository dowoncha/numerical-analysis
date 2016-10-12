import numpy as np

def lagrange(x, f, x0):
    # x array of xi
    # y array of fi
    # x0 value to interpolate at

    result = 0.0;
    lagrange = 0.0;

    for xi in x:
        lagrange *= (x0 - xi)

    return result
