
import numpy as np
import matplotlib.pyplot as plt
import random




def uniform_pseudo_random_generator(x_n, N, xMin, xMax):
    randlist = np.empty(N) 
    for i in range (N):
        randlist[i] = int( (random.random ()) * (xMax - xMin) ) + xMin
        #print (i, randlist[i])
    return randlist
    

def main():
    x_coord = uniform_pseudo_random_generator(5, 500, 0, 100)
    x_bins = np.linspace(0,101)
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.hist(x_coord)
    plt.show()

if __name__ == "__main__":
    main()
