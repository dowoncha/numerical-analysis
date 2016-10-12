import numpy as np

def evaluate(x, a, z):
    n = len(x)
    p = a[n-1]
    for i in range(n-1, 0, -1):
        p = p * (z - x[i]) + a[i]
    return p

def divdiff(x, y):
    assert len(x) == len(y), "X and Y have mismatching sizes"

    n = len(x)
    t = np.zeros(n)
    a = np.zeros(n)
    for i in range(n):
        t[i] = y[i]
        for j in range(i-1, 0, -1):
            t[j] = (t[j+1] - t[j]) / (x[i] - x[j])
        a[i] = t[0]

    return a

if __name__ == "__main__":
    print "Interpolation module"
    # sin(x)
    def fn(z):
        return z * z # np.sin(x);

    n = 20

    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    #x = np.random.power(3, 20) * 50
    y = fn(x)

    # Table of divided differences
    a = divdiff(x, y)
    print x, y, a

    z = 3.0
    result = evaluate(x, a, z)
    print result
    # result = evaluate(a, )
    # print x0, result[0]
