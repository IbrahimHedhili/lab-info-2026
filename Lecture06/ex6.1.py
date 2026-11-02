from zeros_extrema_methods import bisezione
import numpy as np

def main():
    zero = bisezione(np.cos, 0, 4)
    print(f"{zero:.5}")

if __name__ == "__main__":
    main()