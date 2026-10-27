import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt


def main():
    p = 0.5
    n = 20
    x = int(p * n )
    
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

    #cumulative of Binomial
    y_coord = binom_fix.cdf (x_coord)
    line2 = ax2.plot (x_coord, y_coord, marker='o', markersize=8, label='cumulative', color = color2)

    ax1.set_title ("Binomial and it's cumulative function", size=12)
    ax1.set_xlabel ('x')
    ax1.set_ylabel ('pmf',color=color1)

    ax2.set_ylabel ('cdf', color=color2)

    ax1.set_xticks(x_coord)
    
    ax1.set_ylim(0, binom_fix.pmf(x))
    ax2.set_ylim(0, 1)

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper right')

    fig.set_size_inches(13, 7)
    

    plt.tight_layout()
    plt.show ()


if __name__ == "__main__":
    main()

