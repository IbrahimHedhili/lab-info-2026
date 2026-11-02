def factorial(n):
    fact_n = 1
    for i in range(n):
        fact_n *= n-i
    return fact_n

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def main():
    print(factorial(4))
    print(factorial_recursive(4))

if __name__ == "__main__":
    main()