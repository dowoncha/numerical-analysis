import numpy as np
import matplotlib.pyplot as plt

def newtons_interpolate(xi, yi):
    print points.dtype.name

    # assert points.ndim == 2

    y = x

    return y

if __name__ == "__main__":
    # Test function f(x) = sin(x) / x
    def f(x):
        return np.sin(x) / x

    # Number of interpolation points
    # e.g. 5, 20, 50, 100
    n = 5

    # Generate interpolation points from [0,pi/2]
    xi = np.linspace(0.0, np.pi / 2, n)
    yi = f(xi)
    print xi, yi

    result = newtons_interpolate(xi, yi)

    # Build newton divided differences
    # Evaluate polynomial using nested multiplication

    # Plot yi - P(xi)
    # plt.plot(yi - p(xi))
    # plt.show()
