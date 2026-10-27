import numpy as np
def main():
    file_name = 'eventi_unif.txt'
    with open (file_name) as input_file:
        sample = [float (x) for x in input_file.readlines()]

    print("Statistics from data in file: ", file_name, "\nmean = " ,np.mean(sample)
          ,"\nvaraince = ", np.var(sample, ddof = 1), 
          "\nstd deviation = ", np.std(sample, ddof=1),
          "\nstd deviation from the mean = ", np.std(sample, ddof=1)/ np.sqrt(len(sample)))

if __name__ == "__main__":
    main()