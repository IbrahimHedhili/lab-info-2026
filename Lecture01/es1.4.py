"""
Write a program that, by using a for loop, 
returns the Fibonacci sequence up to the n-th term and stores it in a python dictionary, 
where the key represents the index of each element and value its actual value.
"""


def fibonacci(n):
    fib = {0: 0, 1: 1}
    for i in range(2,n,1):
        c = fib[i-1] + fib[i-2]
        fib[i] = c
    return fib


N = int(input("Fibonacci sequenze to the term: "))
fibo = fibonacci(N)

print(fibo)
