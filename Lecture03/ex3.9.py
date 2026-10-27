import numpy as np
from scipy.stats import norm


def main():
    mean = 0
    sigma = 1
    x = mean + sigma
    norm_fix = norm (mean, sigma)
    print("\N{GREEK CAPITAL LETTER PHI}")
    print("\N{GREEK SMALL LETTER PHI}")
    print(F"Area outside n\N{GREEK SMALL LETTER SIGMA} from the mean in a normal distribution (with \N{GREEK SMALL LETTER MU} = {mean} and \N{GREEK SMALL LETTER SIGMA} = {sigma}): ")
    for i in range(1,6):
        print(f"{i} \N{GREEK SMALL LETTER SIGMA} -> Area = " + f"{2*norm_fix.cdf(mean - i * sigma):.4}")
    

if __name__ == "__main__":
    main()




    
    

