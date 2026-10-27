import numpy as np
import mystatistics as stat
def main():

    #an_array = np.random.random(size = 100) * 100 #simpler but les accurate random generator
    an_array = stat.crea_float_casuali(0., 100., 100, 2, 1)
    print(an_array)
    a_mean = stat.mean(an_array)
    a_var = stat.variance(an_array)
    a_stddev = stat.standarddeviation(an_array)
    a_stddevmean = stat.stdmean(an_array)
    print(f"\nmean : {a_mean:.5} \nvariance : {a_var:.5} \nstandard deviation : {a_stddev:.5} \nstandard deviation from the mean : {a_stddevmean:.5}")

if __name__ == "__main__":
    main()