import numpy as np
from scipy.stats import poisson
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider




def main():
    mu = 5
    n = 50
    poisson_fix = poisson(mu)
    x = 10
    print(f"x = {x} -> expon(x) = {poisson_fix.pmf(x):.4}")
    print(f"x = {x} -> expon(x) = {poisson.pmf(x, mu):.4}")

    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    fig.subplots_adjust(bottom=0.25)#leaving space at the bottom for sliders

    x_coord = np.arange (0, n)
    y_coord = poisson.pmf (x_coord, mu)
    mean, var, skew, kurt = poisson_fix.stats (moments='mvsk')
    print ("mean = ",mean, "variance = ", var, "skewness = ", skew, "kurtosis = ", kurt)
    line, = ax.plot (x_coord, y_coord, marker='o', markersize=8, label='Poisson')

    x_coord1 = np.linspace(0, n, 500)
    y_coord = norm.pdf(x_coord1, mean, np.sqrt(var))
    gaussian, = ax.plot (x_coord1, y_coord, linestyle='dashed', label='Gaussian')
    
    ax.set_title ("Poisson function with several values of it's mean", size=12)
    ax.set_xlabel ('x')
    ax.set_ylabel ('pmf')
    ax.set_xticks(x_coord)
    ax.set_ylim(0,poisson_fix.pmf(mean)*1.1)
    ax.legend(loc='right')
    fig.set_size_inches(13, 7)
    #plt.tight_layout()

    mvsk_text = fig.text(
        x=0.25, 
        y=0.15, 
        s=f"Current values ── Mean: {mu} | Variance: {var:.2} | Skewness: {skew:.4f} | Kurtosis: {kurt:.4f}",
        fontsize=11, 
        fontweight='bold',
        color='darkgreen'
    )

    #SLIDERS
    # 3. creating axis for Slider [x, x, width, hight]
    slider_axis = fig.add_axes([0.25, 0.08, 0.65, 0.03])
    
    # 4. SLider initialization
    slider_mean = Slider(
        ax=slider_axis, 
        label='mean', 
        valmin=0, 
        valmax=50, 
        valinit=mu,
        valstep=1 # Opzionale: definisce lo scatto discreto del cursore
    )

    def reload(val):
        # recover the value of mu from the slider
        m = slider_mean.val
        # updating data
        poisson_fix = poisson(m)
        new_line_data = poisson_fix.pmf (x_coord)
        m, v, sk, k = poisson_fix.stats (moments='mvsk')
        line.set_ydata(new_line_data)

        norm_fix = norm(m, np.sqrt(v))
        gaussian.set_ydata(norm_fix.pdf(x_coord1))
        #
        ax.set_ylim(0,poisson_fix.pmf(m)*1.1)
        #
        mvsk_text.set_text(f"Current values ── Mean: {int(m)} | Variance: {v:.2f} | Skewness: {sk:.4f} | Kurtosis: {k:.4f}")
        # Updating image
        fig.canvas.draw_idle()
    
    slider_mean.on_changed(reload)#linking slider to callback function
    plt.show ()

if __name__ == "__main__":
    main()

