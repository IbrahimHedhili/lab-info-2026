from zeros_extrema_methods import golden_ratio_search_method
from zeros_extrema_methods import golden_ratio_search_method_recursive
import time as tm

def my_function(x):
    return x**2 - 7.3 * x + 4

def main():
    start_tm = tm.time()
    min_1 = golden_ratio_search_method(my_function, -10, 10)
    end_tm = tm.time()
    print("time for golden_ratio_search_method : ",  (end_tm - start_tm)*10**6, "micros")

    start_tm = tm.time()
    min_2 = golden_ratio_search_method_recursive(my_function, -10, 10)
    end_tm = tm.time()
    print("time for golden_ratio_search_method_recursive : ", (end_tm - start_tm)*10**6, "micros")
    
    print(golden_ratio_search_method(my_function, -10, 10))


if __name__ == "__main__":
    main()