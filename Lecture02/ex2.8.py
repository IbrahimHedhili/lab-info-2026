import numpy as np
import matplotlib.pyplot as plt

def func (x) :
    return np.cos (x - np.pi / 2.)


def main () :
    #fig, ax = plt.subplots (nrows = 1, ncols = 3,figsize=(13, 7))
    fig, ax = plt.subplots (nrows = 1, ncols = 3)


    # preparing the set of points to be drawn 
    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.sin (x_coord)

    ax[0].plot (x_coord, y_coord, label='sin (x)')

    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.cos (x_coord)
    #ax[0].plot (x_coord, y_coord, linestyle = 'dashed', label='cos (x)')
    ax[0].plot (x_coord, y_coord, label='cos (x)')

    ax[0].set_title ('Comparing trigonometric \nfunctions', size=12)
    ax[0].set_xlabel ('x')
    ax[0].set_ylabel ('y')
    ax[0].legend ()

    #second subplot
    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.sin (x_coord)
    ax[1].plot (x_coord, y_coord, label='sin x')
    
    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.sin (x_coord - np.pi)
    ax[1].plot (x_coord, y_coord, label=r'sin (x - $\pi$)')

    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.sin (x_coord - np.pi) + 1
    ax[1].plot (x_coord, y_coord, label=r'sin (x - $\pi$) + 1')

    ax[1].set_title ('f(x) = sin(x - A) + B', size=12)
    ax[1].set_xlabel ('x')
    ax[1].set_ylabel ('y')
    ax[1].legend ()


    #third subplot
    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.cos (x_coord)
    ax[2].plot (x_coord, y_coord, label='cos x')
    
    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.sin (x_coord * 4)
    ax[2].plot (x_coord, y_coord, label='cos (4 x)')

    x_coord = np.linspace (0, 2 * np.pi, 10_000)
    y_coord = np.sin (x_coord *4) /2
    ax[2].plot (x_coord, y_coord, label=' cos (4 x)/2 ')

    ax[2].set_title ('f(x) = sin(x - A) + B', size=12)
    ax[2].set_xlabel ('x')
    ax[2].set_ylabel ('y')
    ax[2].legend ()

    fig.set_size_inches(13, 7)

    
    plt.show ()
    


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

    
if __name__ == "__main__":
    main ()