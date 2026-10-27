#!/usr/bin/python3
'''
Write a program that draws the Mandelbrot set with matplotlib.
'''

import matplotlib.pyplot as plt
import numpy as np

def check_if_limited (compl_start, num = 100) :
    
    number = complex (0.0)
    for i in range (num) :
        number = number ** 2 + compl_start
        if abs (number) > 2 :
            return False
    return True        


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


def main():

    xmin = -2.
    xmax = 1.
    ymin = -2.
    ymax = 2.
    resolution = 0.03 

    x_coord = np.arange (xmin, xmax, resolution) 
    y_coord = np.arange (ymin, ymax, resolution) 

    fig, ax = plt.subplots (nrows = 1, ncols = 1)

    ix = 0
    for x in x_coord :
        iy = 0
        for y in y_coord :
            if check_if_limited (complex (x, y)) :
                ax.plot (x, y, marker='o', color = 'black')
            else :   
                ax.plot (x, y, marker='o', color = 'white')
            iy = iy + 1
        ix = ix + 1

    #fig.savefig ('mandel.png',dpi=300)
    plt.show ()

    return

if __name__ == '__main__':
    main()