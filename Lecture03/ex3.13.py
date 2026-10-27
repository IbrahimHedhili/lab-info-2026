import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt


def main():
    p = 1.0 - 0.3173
    n = 10
    x = 10
    
    binom_fix = binom (n, p)

    print(f"x = {x} -> expon(x) = {binom_fix.pmf(x):.4}")


    print(f"x = {x} -> expon(x) = {binom.pmf(x, n,p):.4}")

    
    fig, ax1 = plt.subplots (nrows = 1, ncols = 1)
    ax2 = ax1.twinx()
    color1 = 'Tab:blue'
    color2 = 'Tab:red' 
    #Binomial
    x_coord = np.arange (1, n+1)
    y_coord = binom_fix.pmf (x_coord)
    line1 = ax1.plot (x_coord, y_coord, marker='o', markersize=8, label='Binomial', color = color1)


    ax1.set_title ("Probability that taken 10 measurements of the same quantity expected " \
    "\nto be Gaussian x of them fall within an interval of 1 standard deviation ", size=12)
    ax1.set_xlabel ('x')
    ax1.set_ylabel ('pmf')

    ax1.set_xticks(x_coord)
    
    ax1.set_ylim(0, 0.4)

    ax1.legend(loc='upper right')

    fig.set_size_inches(13, 7)
    
    plt.tight_layout()
    plt.show ()


if __name__ == "__main__":
    main()

