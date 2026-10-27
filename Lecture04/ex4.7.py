import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(5)
def rand_generator(N):
    rand_l = np.full(N, None)
    for i in range(N):
        rand_l[i] = random.random()
    return rand_l

def np_sum(an_array, start, n):
    sum = 0
    for i in range(n):
        sum += an_array[start + i]
    return sum

def main():
    N = 1_000_000
    xMin = 0
    xMax = 1
    randlist = rand_generator(N)

    x_list_2 = []
    for i in range(1, N):
        x_list_2.append( (randlist[i-1]+ randlist[i])/2)
    x_coord_n2 = np.array(x_list_2)

    x_list_4 = []
    for i in range(N-4):
        x_list_4.append( (np_sum(randlist, i, 4))/4)
    x_coord_n4 = np.array(x_list_4)

    x_list_10 = []
    for i in range(N-10):
        x_list_10.append( (np_sum(randlist, i, 10))/10)
    x_coord_n10 = np.array(x_list_10)

    fig, ax = plt.subplots(nrows = 1, ncols = 4)
    x_bins = np.linspace(xMin, xMax, int(np.sqrt(N)/10))
    ax[0].hist(randlist, bins = x_bins)
    ax[1].hist(x_coord_n2, bins = x_bins)
    ax[2].hist(x_coord_n4, bins = x_bins)
    ax[3].hist(x_coord_n10, bins = x_bins)

    fig.set_size_inches(13, 7)
    plt.show()


if __name__ == "__main__":
    main()