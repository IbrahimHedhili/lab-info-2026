import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import numpy as np

x = np.linspace(0, 10, 400)
a = 1.0  # parametro variabile
y = np.sin(a * x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

cursor = Cursor(ax, horizOn=False, vertOn=True, color='red')

def on_move(event):
    global a
    if event.inaxes == ax:
        a = event.xdata / 5   # esempio: parametro dipende dal cursore
        line.set_ydata(np.sin(a * x))
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', on_move)
plt.show()