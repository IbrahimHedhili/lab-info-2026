"""Write a program that, by using a while loop, 
returns the Fibonacci sequence up to the n-th term 
and stores it in a python list."""


def fibonacci(n):
    fib = [0,1]
    while(len(fib) < n):
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib

N = int(input("Fibonacci sequenze to the term: "))
fib = fibonacci(N)

print(fib[0:N:1])

