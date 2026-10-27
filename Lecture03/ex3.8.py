import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt


def main():
    mean = 0
    sigma = 1
    x = mean + sigma
    expon_fix = expon (mean, sigma)

    print(f"x = {x} -> expon(x) = {expon_fix.pdf(x):.4}")

    x = mean - sigma
    print(f"x = {x} -> expon(x) = {expon.pdf(x, mean, sigma):.4}")

    

    fig, ax1 = plt.subplots (nrows = 1, ncols = 1)
    ax2 = ax1.twinx()
    color1 = 'Tab:blue'
    color2 = 'Tab:red' 
    #Exponential
    x_coord = np.linspace (mean, mean + 6*sigma, 10_000)
    y_coord = expon_fix.pdf (x_coord)
    line1 = ax1.plot (x_coord, y_coord, label='Exponential', color = color1)

    #cumulative of Exponential
    y_coord = expon_fix.cdf (x_coord)
    line2 = ax2.plot (x_coord, y_coord, label='cumulative', color = color2)

    #vertical reference
    x_coord = np.full(100, mean)
    y_coord = np.linspace (0, expon_fix.pdf(mean), 100)
    ax1.plot (x_coord, y_coord, linestyle = 'dashed', color = 'grey')

    ax1.set_title ("Exponential and it's cumulative function", size=12)
    ax1.set_xlabel ('x')
    ax1.set_ylabel ('pdf',color=color1)

    ax2.set_ylabel ('cdf', color=color2)
    
    ax1.set_ylim(0, expon_fix.pdf(mean))
    ax2.set_ylim(0, 1)

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper right')

    fig.set_size_inches(13, 7)

    plt.tight_layout()
    plt.show ()


if __name__ == "__main__":
    main()




    
    

