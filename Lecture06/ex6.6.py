from zeros_extrema_methods import golden_ratio_search_method
from zeros_extrema_methods import golden_ratio_search_method_recursive
from zeros_extrema_methods import golden_ratio_search_method_maximum_recursive
import time as tm
import matplotlib.pyplot as plt
import numpy as np

def my_function(x):
    return -1 * x**2 - 7.3 * x + 4

def minus_function(x):
    return -1 * my_function(x)

def main():
    xMax = 10
    xMin = -10
    start_tm = tm.time()
    min_1 = golden_ratio_search_method(minus_function, xMin, xMax)
    end_tm = tm.time()
    print("time for golden_ratio_search_method : ",  (end_tm - start_tm)*10**6, "micros")

    start_tm = tm.time()
    min_2 = golden_ratio_search_method_maximum_recursive(my_function, xMin, xMax)
    end_tm = tm.time()
    print("time for golden_ratio_search_method_recursive : ", (end_tm - start_tm)*10**6, "micros")
    
    print(golden_ratio_search_method_maximum_recursive(my_function, xMin, xMax))

    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    N = 10_000
    x_coord = np.linspace (xMin, xMax, N)
    y_coord = my_function(x_coord)
    ax.plot (x_coord, y_coord, label='')
    y_coord = minus_function(x_coord)
    ax.plot (x_coord, y_coord, label='')
    #ax.set_ylim(0,1.1)

    plt.show()

if __name__ == "__main__":
    main()