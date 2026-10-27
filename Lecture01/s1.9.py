"""Write a python program that finds the decomposition in prime factors of a positive integer number, implementing the algorithm in a function encapsulated in a python module

Write a test function, in the library, that checks the correctness of the procedure for all numbers from 1 to 100"""

from functions import primeNumbers

if __name__ == "__main__":

    primesFactors = {}

    primeF = []
    a = int(input("Provide an integer number : "))

    b = a

    primes = primeNumbers(a)

    for i in primes:
        primesFactors[i] = 0
    print(primes)
    print(primesFactors)

    rest = None

    while b != 1 :
        for i in primes:
            if i > 1:
                if b % i == 0:
                    b = b/i 
                    primesFactors[i] +=1 
                    primeF.append(i)

    print(primesFactors)

    factorisation = {}
    for i in primesFactors.keys():
        if primesFactors[i] !=0:
            factorisation[i] = primesFactors[i]

    print(factorisation)

    solution = f"The decomposition in prime factors of {a} is a = "
    primeStr = f""
    for i in range(len(primeF)):
        primeStr += f"{primeF[i -1]}"
        if i < len(primeF) - 1: primeStr += " * "

    #solution += primeStr

    print(solution + primeStr)

    
