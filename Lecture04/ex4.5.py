import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm
import math

random.seed(5)

def sturges (N_events) :
    return int( np.ceil( 1 + np.log2(N_events) ) )

def single_uniform_pseudo_random_generator(xMin, xMax):
    randNum = random.random() * (xMax - xMin) + xMin 
    return randNum
    
def TAC_pseudo_random_number_generator (pdf, xMin, xMax, N):
    randpdf = np.empty(N)

    i=0
    while i < N :
        x = single_uniform_pseudo_random_generator(xMin, xMax)
        y = single_uniform_pseudo_random_generator(0, 1)
        if (pdf(x) > y):
            randpdf[i] = x
            i += 1
    
    return randpdf
    
def normarl_distribution_pdf(x):
    return(norm.pdf(x, 0, 1))

def main():
    N = 10000
    xMin = -5
    xMax = 5
    x_coord = TAC_pseudo_random_number_generator(normarl_distribution_pdf, xMin, xMax, N)
    x_bins = np.linspace(xMin, xMax, int(math.sqrt(N/3)))
    fig, ax = plt.subplots(nrows = 1, ncols = 1)

    ax.hist(x_coord, bins = x_bins)
    plt.show()

if __name__ == "__main__":
    main()
