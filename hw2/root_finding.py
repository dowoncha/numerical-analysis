# Dowon Cha
# Math 566 - Numerical Analysis
# 9/11/16
# Solving e^x - 3x^2 = 0 using newtons's method
import math

def bisection(f, low, high, eps):
    assert f(low) * f(high) < 0

    # for i in range(50):
    # Eps not being used properly
    while high - low > eps:
        midpoint = (low + high) / 2

        if f(midpoint) * f(low) > 0:
            low = midpoint
        else:
            high = midpoint
    return midpoint

# Newtons method
# f function to evaluate
# df derivative of f
# x0 initial guess
# eps epsilon error
def newtons(f, df, x0, eps):
    # Run until value of estimated x is less than eps
    while abs(f(x0)) > eps:
        x1 = x0 - f(x0) / df(x0)
        print 'Error:', abs(x1 - x0)
        x0 = x1

    return x0

# Secant method
def secant(f, x0, x1, eps):
    while abs(f(x1)) > eps:
        x2 = x1 - f(x1) * ((x1-x0)/(f(x1)-f(x0)))
        print 'Error:', abs(x2 - x1)
        x0 = x1
        x1 = x2
    return x1

if __name__ == "__main__":
    # f(x) = e^x - 3x^2
    def f(x):
        return math.exp(x) - 3 * x * x

    # df/dx = e^x - 6x
    def df(x):
        return math.exp(x) - 6 * x

    eps = 1e-12

    root = bisection(f, 0., 1., eps)
    print 'Bisection, initial guess x=[0:1]', root, f(root)

    root = newtons(f, df, 0., eps)
    print 'Newtons method, initial guess x = 0: ', root, f(root)

    root = newtons(f, df, 1., eps)
    print 'Newtons method, initial guess x = 1: ', root, f(root)

    root = secant(f, 0., 1., eps)
    print 'Secant method, for x:[0,1]', root, f(root)
