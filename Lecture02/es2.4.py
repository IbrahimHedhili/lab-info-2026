import time
import numpy as np
#time_snapshot = time.time ()
#print (time_snapshot)
for i in (1_000, 2_000, 5_000, 10_000, 100_000, 1_000_000):
    start_time = time.time()

    a_list1 = range(i)
    a_list2 = range(i)
    #sum
    result = np.add(a_list1, a_list2).tolist()
    end_time = time.time()
    elapsed_time = (end_time - start_time)*1_000
    print(f"time to perform the sum of two lists of {i} elements {elapsed_time} millis")

    #arrays
    start_time = time.time()
    arr1 = np.array(a_list1)
    arr2 = np.array(a_list2)
    #sum
    result2 = arr1 + arr2
    end_time = time.time()
    elapsed_time = (end_time - start_time)*1_000
    print(f"time to perform the sum of two arrays of {i} elements {elapsed_time} millis")

