import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Funzione iniziale: y = a * sin(b * x)
def funzione(x, a, b):
    return a * np.sin(b * x)

# Dati iniziali
x = np.linspace(0, 10, 500)
a_init = 1.0
b_init = 1.0
y = funzione(x, a_init, b_init)

# Creazione della figura e del grafico
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)  # spazio per i cursori
linea, = ax.plot(x, y, lw=2)
ax.set_title("Grafico interattivo con cursori")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Posizione e dimensione dei cursori
ax_a = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor="lightgoldenrodyellow")
ax_b = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor="lightgoldenrodyellow")

# Creazione dei cursori
slider_a = Slider(ax_a, 'Ampiezza (a)', 0.1, 5.0, valinit=a_init)
slider_b = Slider(ax_b, 'Frequenza (b)', 0.1, 5.0, valinit=b_init)

# Funzione di aggiornamento
def aggiorna(val):
    a = slider_a.val
    b = slider_b.val
    linea.set_ydata(funzione(x, a, b))
    fig.canvas.draw_idle()  # aggiorna il grafico

# Collegamento dei cursori alla funzione di aggiornamento
slider_a.on_changed(aggiorna)
slider_b.on_changed(aggiorna)

plt.show()

from matplotlib.widgets import Cursor

fig, ax = plt.subplots()
ax.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)))
cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
plt.show()
