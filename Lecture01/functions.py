def fibonacci(n):
    fib = [0,1]
    while(len(fib) < n):
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib

def primeNumbers(p):
    primeNum = [2]
    for i in range(2,p+1):
        for n in primeNum:
            x = i % n
            if i%n == 0: break
            if n == primeNum[len(primeNum)-1]: primeNum.append(i) 
    
    primeNum.sort(reverse=True)
    primeNum.append(1)
    primeNum.sort()
    return primeNum