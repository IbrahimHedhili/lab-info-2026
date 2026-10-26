import numpy as np
from statistics import stdev
import numpy as np

def main():
    with open ('eventi_unif.txt') as input_file:
        sample = [float (x) for x in input_file.readlines()]

    nsample = np.array(sample)
    print("number of events : ",len(sample))
    print("min = ", np.amin(sample), "\nmax = ", np.amax(sample))
    print(type(sample))
    mean = sum(sample) / len(sample)
    larger = lambda x : x < mean
    larger_list = list(filter(larger, sample))
    smaller = lambda x: x > mean
    smaller_list = list(filter(smaller, sample))
    print(len(smaller_list))
    print(len(larger_list))
    print(f"stdev of sample: {stdev(sample):.4}")
    print(f"stdev of smaller than mean: {stdev(smaller_list):.4}, x2 = {stdev(smaller_list)*2:.4}")
    print(f"stdev of greater than mean: {stdev(larger_list):.4}, x2 = {stdev(larger_list)*2:.4}")
    print(f"mean of sample = {mean:.4}")
    print(f"stdev of smaple = {np.std(nsample, ddof=1):.4}")


if __name__ == "__main__":
    main()