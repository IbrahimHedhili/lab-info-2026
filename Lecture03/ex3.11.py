import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt


def main():
    mu = 5
    n = 20
    poisson_fix = poisson(mu)
    x = 10
    print(f"x = {x} -> expon(x) = {poisson_fix.pmf(x):.4}")


    print(f"x = {x} -> expon(x) = {poisson.pmf(x, mu):.4}")

    
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    x_coord = np.arange (0, n)

    for i in range(1,5):
        
        y_coord = poisson.pmf (x_coord, i)
        ax.plot (x_coord, y_coord, marker='o', markersize=8, label=f'Poisson mu = {i}')




    ax.set_title ("Poisson function with several values of it's mean", size=12)
    ax.set_xlabel ('x')
    ax.set_ylabel ('pmf')

    ax.set_xticks(x_coord)
    
    ax.set_ylim(0, 0.5)

    ax.legend( loc='right')

    fig.set_size_inches(13, 7)
    

    plt.tight_layout()
    plt.show ()


if __name__ == "__main__":
    main()

