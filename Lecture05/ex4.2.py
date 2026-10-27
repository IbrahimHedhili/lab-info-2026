import numpy as np

class linear_congruential_generator:
    """
    A linear congruential generator
    """
    def __init__(self, seed=0):
        M = 2147483647
        A = 214013
        C = 2531011
        if seed < 0 or seed > M:
            raise ValueError("seed must be between 0 and M")
        if type(seed) != int and type(seed) != float:
            raise ValueError("seed must be float or integer")
        
        self.M = 2147483647
        self.A = 214013
        self.C = 2531011
        self.x_n = seed
        self.seed = seed

    def setSeed(self, seed):
        self.seed = seed
    def getSeed(self):
        return self.seed
    def getxn(self):
        return self.x_n
    def restart(self):
        self.x_n = self.seed
    
    def generate(self):
        self.x_n = ((self.A * self.x_n + self.C) % self.M)
        return self.x_n
    def generate(self, n):
        a_rand = np.ones(n)
        for i in range(n):
            self.x_n = ((self.A * self.x_n + self.C) % self.M)
            a_rand[i] = self.x_n
        return a_rand

def main():
    a = 0

if __name__ == "__main__":
    main()