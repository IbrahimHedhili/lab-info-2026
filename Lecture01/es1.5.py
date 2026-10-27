from functions import fibonacci


if __name__ == "__main__":

    N = int(input("Fibonacci sequenze to the term: "))
    fib = fibonacci(N)
    print(fib[0:N:1])

    fibEven = fib[0:N:2]
    print(fibEven)

    fibOdd = fib[1:N:2]
    print(fibOdd)