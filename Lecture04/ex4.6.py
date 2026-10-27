import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
import random
from numba import jit, prange


random.seed(5)

def inverse_expon_cdf(x, scale):
    return -1 * np.log(1 - x) / scale

@jit(nopython=True, parallel=True)
def rand_generator(N):
    rand_l = np.zeros(N)
    for i in prange(N):
        rand_l[i] = random.random()
    return rand_l

def main():
    loc = 0
    scale = 1
    expon_fix = expon(loc, scale)
    xMax = loc + 6 * scale
    xMin = loc
    N = 1_000_000
    rand_list = rand_generator(N)

    inverse_rand_list = inverse_expon_cdf(rand_list, scale)

    fig, ax = plt.subplots(nrows = 1, ncols = 2)

    x_coord = np.linspace (xMin, xMax, 10_000)
    y_coord = expon_fix.pdf (x_coord)
    ax[0].plot (x_coord, y_coord, label='Exponential')
    ax[0].set_ylim(0,1.1)

    x_bins = np.linspace(xMin, xMax, int(np.sqrt(N/3)))
    ax[1].hist(inverse_rand_list, bins = x_bins)

    plt.show()


if __name__ == "__main__":
    main()