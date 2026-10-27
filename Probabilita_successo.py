import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt


def main():
    p = 0.01
    n = 30
    m = 5

    print(f"probabilità di avere successo con una azienda dopo aver creato {20} aziende: {binom.pmf(1, 20, p)}")
    color1 = "Tab:blue"
    fig, ax1 = plt.subplots (nrows = 1, ncols = 1)

    
    x_coord = np.linspace(m, m * n, n)
    y_coord = np.full(n, 1)
    for i in range(n):
        value =  int(binom.pmf(1, int((i+1) * m), p) * 100) 
        y_coord[i] = value
        print(f" Probability to succede 1 time after trying {(i+1) * m} times: {y_coord} ")
    
    line1 = ax1.plot (x_coord, y_coord, marker='o', markersize=8, label='Binomial', color = color1)

    ax1.set_title ("Probability of 1 success after x trials", size=12)
    ax1.set_xlabel ('x')
    ax1.set_ylabel ('probability',color=color1)

    ax1.set_xticks(x_coord)
    
    ax1.set_ylim(0, np.amax(y_coord) * 1.05 )

    ax1.legend(loc='upper right')

    fig.set_size_inches(13, 7)
    
    plt.tight_layout()
    plt.show ()


if __name__ == "__main__":
    main()

