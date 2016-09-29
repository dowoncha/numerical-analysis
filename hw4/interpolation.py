import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def evaluate(c, x, r):
    # c : array of coeffecients
    # x : array x values

    n = len(c) - 1

    # interpolated y-value
    # Nested multiplication of the polynomial
    out = c[n]
    for i in range( n-1, -1, -1):
        out = out * ( r - x[i] ) + c[i]
    return out

def coefficients(x, y):
    # x : array of x values
    # y : array of f(x) values
    # returns np array of interpolated coefficients

    # assert points.ndim == 2
    n = len(x)
    c = []

    for i in range(n):
        c.append(y[i])

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            c[j] = ( c[j] - c[j-1] ) / ( x[j] - x[j - i])

    return np.array(c)

if __name__ == "__main__":
    # Test function f(x) = sin(x) / x
    def f(x):
        return np.sin(x) / x # np.float64(x)

    # Number of interpolation points
    # e.g. 5, 20, 50, 100
    n = 20

    # Generate interpolation points from [0,pi/2]
    xi = np.linspace(0.0, np.pi / 2.0, n)
    yi = f(xi)
    print xi, "\n", yi

    coefs = coefficients(xi, yi)
    interpolated = evaluate(coefs, xi, 0.0)
    print coefs, interpolated

    inhouse = sp.Interpolate.BarycentricInterpolator(xi, yi)
    print "Inhouse", inhouse

    # Build newton divided differences
    # Evaluate polynomial using nested multiplication

    # Plot yi - P(xi)
    plt.plot(yi - f(xi))
    plt.show()
