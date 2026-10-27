M = 2147483647
A = 214013
C = 2531011
import time
import numpy as np
def linear_congruential_generator(x_n, N):
    x = [None] * N
    for i in range(1,N):
        x[i] = ((A * x_n + C) % M)
        x_n = x[i]
    return x
    
def main():
    print(linear_congruential_generator(int(time.time()), 100))

if __name__ == "__main__":
    main()