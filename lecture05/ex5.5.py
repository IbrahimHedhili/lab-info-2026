import numpy as np
import matplotlib.pyplot as plt
def sturges (N_events) :
    return int( np.ceil( 1 + np.log2(N_events) ) )

def main():
    with open ('eventi_gauss.txt') as input_file:
        sample = [float (x) for x in input_file.readlines()]
    N = len(sample)
    cube_list = list(map(lambda x: x**3, sample))
    square_list = list(map(lambda x: x**2, sample))

    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    N_bins = 125
    bin_edges = np.linspace (np.amin(cube_list), np.amax(cube_list), N_bins)
    ax.hist (square_list,bins=bin_edges, histtype = "step", linewidth = 2,
                 color = 'orange', label = "x^2")
    ax.hist (cube_list,bins=bin_edges, histtype = "step", linewidth = 2,
                 color = 'blue', label = "x^3")
    ax.hist (sample,bins=bin_edges, histtype = "step", linewidth = 2,
             color = 'grey', label = "x")
    
    
    ax.legend()
    plt.show()
if __name__ == "__main__":
    main()