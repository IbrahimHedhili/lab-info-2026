
if __name__ == "__main__":

    primeNumbers = [2]
    for i in range(2,100):
        for n in primeNumbers:
            x = i % n
            if i%n == 0: break
            if n == primeNumbers[len(primeNumbers)-1]: primeNumbers.append(i) 

    primeNumbers.sort(reverse=True)
    primeNumbers.append(1)
    primeNumbers.sort()
    print(primeNumbers)
        
    
        
                