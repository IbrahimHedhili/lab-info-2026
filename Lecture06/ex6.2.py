from zeros_extrema_methods import bisezione
from zeros_extrema_methods import bisezione_ricorsiva
import numpy as np
import time as tm

def main():
    start_tm = tm.time()
    zero_1 = bisezione(np.cos, 0, 4)
    end_tm = tm.time()
    print("time for simple bisection method : ",  (end_tm - start_tm)*10**6, "micros")

    start_tm = tm.time()
    zero_2 = bisezione(np.cos, 0, 4)
    end_tm = tm.time()
    print("time for recursive bisection method : ", (end_tm - start_tm)*10**6, "micros")
    
if __name__ == "__main__":
    main()