import numpy as np
from nevilles import *

if __name__ == "__main__":
    print "Interpolation module"
    # sin(x)
    def fn(x):
        return np.sin(x);

    x = np.random.power(3, 1000)
    f = fn(x)

    result = nevilles(x, f, 0);
    print result
