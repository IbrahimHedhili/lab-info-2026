import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Creazione dei dati iniziali
t = np.linspace(0.0, 1.0, 1000)
frequenza_iniziale = 3.0
ampiezza_iniziale = 1
s = np.sin(2 * np.pi * frequenza_iniziale * t) * ampiezza_iniziale

# 2. Configurazione di Figura e Assi principali
fig, ax = plt.subplots()
# Lasciamo dello spazio in basso per ospitare lo slider ed evitare sovrapposizioni
fig.subplots_adjust(bottom=0.50)

# Tracciamo la linea iniziale e salviamo il riferimento dell'oggetto ('linea')
linea, = ax.plot(t, s, lw=10, color='blue')
# ax.plot(...) restituisce una lista, con la virgola davanti a 
#linea si assegna il primo valore della lista a linea, quindi linea diventa
#un oggetto 2D
ax.set_ylim(-ampiezza_iniziale*1.05, ampiezza_iniziale*1.05)

ax.set_xlabel('Tempo [s]')
ax.set_ylabel('Ampiezza')
ax.set_title('Grafico Interattivo con Slider')

# 3. Creazione degli assi per lo Slider [posizione_x, posizione_y, larghezza, altezza]
assi_slider = fig.add_axes([0.25, 0.1, 0.65, 0.03])
assi_slider2 = fig.add_axes([0.25, 0.25, 0.65, 0.03])
# 4. Inizializzazione dello Slider
slider_frequenza = Slider(
    ax=assi_slider2, 
    label='Frequenza [Hz]', 
    valmin=0.0, 
    valmax=30.0, 
    valinit=frequenza_iniziale,
    valstep=0.5 # Opzionale: definisce lo scatto discreto del cursore
)
# 4. Inizializzazione dello Slider ampiezza
slider_ampiezza = Slider(
    ax=assi_slider, 
    label='Ampiezza', 
    valmin=0.0, 
    valmax=30.0, 
    valinit=ampiezza_iniziale,
    valstep=0.5 # Opzionale: definisce lo scatto discreto del cursore
)

# 5. Definizione della funzione di aggiornamento (Callback)
def aggiorna(val):
    # Recuperiamo il valore attuale dello slider frequenza
    freq = slider_frequenza.val
    # Recuperiamo il valore attuale dello slider ampieza
    amp = slider_ampiezza.val
    # Aggiorniamo i dati dell'asse Y della linea preesistente
    new_data = np.sin(2 * np.pi * freq * t) * amp
    linea.set_ydata(new_data)
    #
    ax.set_ylim(-amp*1.05, amp*1.05)
    # Ridisegniamo la figura in modo efficiente
    fig.canvas.draw_idle()

# 6. Collegamento dello slider alla funzione di callback
slider_frequenza.on_changed(aggiorna)
slider_ampiezza.on_changed(aggiorna)

plt.show()
