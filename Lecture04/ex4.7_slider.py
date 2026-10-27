import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Slider
from scipy.stats import norm
from math import sqrt

random.seed(5)
def sturges (N_events) :
    return int( np.ceil( 1 + np.log2(N_events) ) )

def rand_generator(N):
    rand_l = np.full(N, None)
    for i in range(N):
        rand_l[i] = random.random()
    return rand_l


def discrete_gaussian_from_linear_values(randlist, n ):
    x_coord_n = np.empty(len(randlist) - n)
    for i in range(len(randlist)- n):
        x_coord_n[i] = ( (np.sum(randlist[i:i+n]))/n)
    return x_coord_n


def main():
    N = 1_000
    xMin = -0.75
    xMax = 0.75
    randlist = rand_generator(N) * (xMax - xMin) + xMin
    x_coord_2 = discrete_gaussian_from_linear_values(randlist, 2)

    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    fig.set_size_inches(13, 7)
    fig.subplots_adjust(bottom = 0.25)#leaving space at the bottom for sliders
    x_bins = np.linspace(xMin, xMax, int(sqrt(N*2)))
    countings, bin_edges, bars = ax.hist(x_coord_2, bins = x_bins)
    state = {'bars': bars}

    mean = (xMax - xMin) / 2 + xMin
    sigma = (xMax - xMin) / 12
    norm_fix = norm(mean, sigma)
    x_coord_norm = np.linspace(xMin, xMax, 10_000)
    y_coord_norm = norm_fix.pdf(x_coord_norm)
    ax1 = ax.twinx()
    ax1.plot(x_coord_norm, y_coord_norm)
    ax1.set_ylim(0, norm_fix.pdf(mean)*1.1)


    #SLIDERS
    # 3. creating axis for Slider [x, x, width, hight]
    slider_axis = fig.add_axes([0.25, 0.08, 0.65, 0.03])
    
    # 4. SLider initialization
    slider_mean = Slider(
        ax=slider_axis, 
        label='mean', 
        valmin=1, 
        valmax=50, 
        valinit=2,
        valstep=1 # Opzionale: definisce lo scatto discreto del cursore
    )

    def reload(val):
        # recover the value of mu from the slider
        new_value = int(slider_mean.val)
        x_coord = discrete_gaussian_from_linear_values(randlist, new_value)

        # updating data
        for bar in state['bars']:
            bar.remove()
        countings, bin_edges, new_bars = ax.hist(x_coord, bins = x_bins)
        state['bars'] = new_bars

        # Updating image
        fig.canvas.draw_idle()
    
    slider_mean.on_changed(reload)#linking slider to callback function
    plt.show()


if __name__ == "__main__":
    main()