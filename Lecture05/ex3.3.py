import numpy as np
import matplotlib.pyplot as plt
def sturges (N_events) :
    return int( np.ceil( 1 + np.log2(N_events) ) )

def main():
    with open ('eventi_gauss.txt') as input_file:
        sample = [float (x) for x in input_file.readlines()]
    N = int(input("The histogram will be filled with the first N numbers contained in the file \nN = "))
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    N_bins = sturges(N)
    bin_edges = np.linspace (np.amin(sample[0:N]), np.amax(sample[0:N]), N_bins)
    ax.hist (sample[0:N],bins=bin_edges,
             color = 'orange')
    plt.show()
if __name__ == "__main__":
    main()