# Multivariate newton's method
# f1(x,y) = 4x^2 + y^2 - 14
# f2(x,y) = x + y - sin(x - y)

import math

def newtons(f, df, x0, eps):
    # Run until value of estimated x is less than eps
    while abs(f(x0)) > eps:
        x0 = x0 - f(x0) / df(x0)
        # x0 = x1

    return x0

if __name__ == "__main__":
    # Test functions
    f1 = lambda x1, x2: 4*x1*x1 + x2*x2 - 14
    f2 = lambda x1, x2: x1 + x2 - math.sin(x1 - x2)

    # Derivatives for the Jacobian
    df1x1 = lambda x1, x2: 8 * x1
    df1x2 = lambda x1, x2: 4 + 2*x2
    df2x1 = lambda x1, x2: 1 - math.cos(x1 - x2)
    df2x2 = lambda x1, x2: 1 + math.cos(-x2)
