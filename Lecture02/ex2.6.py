import numpy as np
from mystatistics import percentile25
from mystatistics import percentile
def main():
    an_array = np.arange(1,101) #from 0 to 100
    print(an_array)

    p_25 = percentile25(an_array)
    print(f"top 25% : {p_25[0]} \nbottom 25% : {p_25[1]}")

    p = int(input("Provide a percentile: "))
    p_x = percentile(an_array, p)
    print(f"top {p}% : {p_x[0]} \nbottom {p}% : {p_x[1]}")

if __name__ == "__main__":
    main()