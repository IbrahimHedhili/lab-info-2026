class linear_congruential_generator:
    """
    A linear congruential generator
    """
    def __init__(self, seed=0):
        if seed < 0:
            raise ValueError("seed can't be negative")
        if type(seed) != int:
            if type(seed) == float:
            else raise ValueError("seed must be float or integer")

        self.seed = seed

    def setSeed(self, seed):
        self.seed = seed
    def getSeed(self):
        return self.seed

def main():
    a = 0

if __name__ == "__main__":
    main()