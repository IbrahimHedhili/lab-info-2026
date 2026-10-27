import time
import numpy as np
from mystatistics import median

def main():
    an_array = np.array([4,7,3,1,8,0,12,1])
    print(f"before sort: {an_array}")
    #sort
    sorted_array = np.sort(an_array)
    print(f"after sort: {sorted_array}")
    #median
    print(f"median: {median(an_array)}")

    odd_array = np.array([4,7,3,1,0,2,1])
    print(f"before sort: {odd_array}")
    #sort
    sorted_odd_array = np.sort(odd_array)
    print(f"after sort: {sorted_odd_array}")
    #median
    print(f"median: {median(odd_array)}")

    #second part
    for i in (1_000, 2_000, 5_000, 10_000, 100_000, 1_000_000, 5_000_000, 10_000_000):
        print(f"Array length: {i}")
        an_array = np.random.randint(1,100,i)

        
        start_time = time.time()
        #median
        result = np.median(an_array)
        end_time = time.time()
        elapsed_time = (end_time - start_time)*1_000
        print(f"numpy: {elapsed_time:.4} millis")

        start_time = time.time()
        #median
        result2 = median(an_array)
        end_time = time.time()
        elapsed_time = (end_time - start_time)*1_000
        print(f"custom library: {elapsed_time:.4} millis")

        print("\n")



if __name__ == "__main__":
    main()