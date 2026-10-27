import numpy as np
import matplotlib.pyplot as plt
def sturges (N_events) :
    return int( np.ceil( 1 + np.log2(N_events) ) )

def main():
    with open ('eventi_gauss.txt') as input_file:
        sample = [float (x) for x in input_file.readlines()]
    
    with open ('eventi_unif.txt') as input_file:
        sample1 = [float (x) for x in input_file.readlines()]
    print("Length first file = ", len(sample), "\nLength second file = ", len(sample1))

    fig, ax = plt.subplots (nrows = 1, ncols = 1)

    N_bins = sturges(int(len(sample) + len(sample1)) / 2)

    min = np.amin(sample) if np.amin(sample) < np.amin(sample1) else np.amin(sample1)
    print("min1 = ", np.amin(sample), "\nmin2 = ", np.amin(sample1))
    max = np.amax(sample) if np.amax(sample) < np.amax(sample1) else np.amax(sample1)
    bin_edges = np.linspace (min, max, N_bins)
    
    ax.hist (sample,bins=bin_edges,color = 'orange')
    ax.hist (sample1,bins=bin_edges,alpha = 0.5, color = 'blue')
    plt.show()
if __name__ == "__main__":
    main()