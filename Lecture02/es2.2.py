import numpy as np

arr = np.arange(1,101)
print(arr)
"""
for i in range(1,100):
    arr[i] = np.sum(np.arange(1,i+1))"""

arr = np.cumsum(arr)
print(arr)