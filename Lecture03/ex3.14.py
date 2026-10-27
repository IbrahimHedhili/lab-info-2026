#!/usr/bin/python
import numpy as np
from scipy.stats import poisson

def main():
    expected_events = 4
    poisson_fix = poisson(4)
    single_counting_probability = 1 - poisson_fix.cdf(4)
    ten_countings_probability = single_counting_probability**10
    print(f"Probability for single counting to be greater than the expected number of events {expected_events}: {single_counting_probability:.4}") 
    print(f"Probability that 10 measurements of the same counting experiment: {ten_countings_probability:.4}")
if __name__ == "__main__":
    main()
