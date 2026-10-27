import math
import statistics
class stats:
    def __init__(self, m_list ):
        if type(m_list) != list :
            raise TypeError("first attribute must be a list")
        
        self.mylist = m_list
        self.mean = statistics.mean(m_list)
        self.var = statistics.variance(m_list)
        self.stdev = statistics.stdev(m_list)
        self.stdevmean = self.stdev / math.sqrt(len(self.mylist))
        self.statsval = [self.mean, self.var, self.stdev, self.stdevmean]

    def statsvalues(self):
        """
        Returns [mean, variance, std dev, std dev from the mean]
        """
        return self.statsval
        
def main():
    with open ('eventi_unif.txt') as input_file:
        sample = stats([float (x) for x in input_file.readlines()])
    print(sample.statsvalues())

if __name__ == "__main__":
    main() 