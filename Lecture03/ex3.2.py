import numpy as np
def main():
    with open ('eventi_unif.txt') as input_file:
        sample = [float (x) for x in input_file.readlines()]

    i = 0
    n = 0
    while(i <10):
        if sample[n] >= 0:  
            print(sample[n])
            i +=1
        n += 1
    print("number of events : ",len(sample))
    print("min = ", np.amin(sample), "\nmax = ", np.amax(sample))
    
if __name__ == "__main__":
    main()