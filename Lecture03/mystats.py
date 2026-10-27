import numpy as np
import matplotlib.pyplot as plt

def sturges (N_events) :
    return int( np.ceil( 1 + np.log2(N_events) ) )

def disp_stats(file_name):
    with open (file_name) as input_file:
        sample = [float (x) for x in input_file.readlines()]

    print("Statistics from data in file: ", file_name, "\nmean = " ,np.mean(sample)
          ,"\nvaraince = ", np.var(sample, ddof = 1), 
          "\nstd deviation = ", np.std(sample, ddof=1),
          "\nstd deviation from the mean = ", np.std(sample, ddof=1)/ np.sqrt(len(sample)))

    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    N_bins = sturges(len(sample))
    bin_edges = np.linspace (np.amin(sample), np.amax(sample), N_bins)
    ax.hist (sample,bins=bin_edges,color = 'orange')
    plt.show()