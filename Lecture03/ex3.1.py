import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    sample = np.array([2,3,5,9,19])
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample,
             color = 'orange')
    script_dir = Path(__file__).parent
    file_path = script_dir / 'figure1.png'
    plt.savefig(file_path)
    plt.show ()
    

if __name__ == "__main__":
    main()