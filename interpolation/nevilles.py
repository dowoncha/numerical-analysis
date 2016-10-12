import numpy as np

def nevilles(x, f, x0):

    t = np.zeros(len(f))
    for i in range(len(x)):
        t[i] = f[i]
        # print "X_%d: %f" % (i, x[i])
        # Start at j=i-1, step -1, until 0
        for j in range(i-1, 0, -1):
            t[j] = t[j+1] + (t[j+1]-t[j]) * (x0 - x[i])/(x[i] - x[j])
    return t

if __name__ == "__main__":
    print "Interpolation module"
    # sin(x)
    def fn(x):
        return x * x# np.sin(x);

    x = np.random.power(3, 20)
    f = fn(x)
    x0 = 3.0

    result = nevilles(x, f, x0);
    print x0, result[0]
