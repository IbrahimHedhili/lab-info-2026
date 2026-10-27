import numpy as np
import matplotlib.pyplot as plt
import math
import time


def i_mandelbrot_matrix(h_res, v_res, max_iterations):

    X, Y = np.meshgrid(np.linspace(-2.0,0.5, h_res), np.linspace(-1.25,1.25, v_res))
    point_grid = X + 1j * Y
    z_n = np.zeros((h_res,v_res))

    z_i = np.full((h_res,v_res), max_iterations)

    Maschera_booleana = np.full((h_res,v_res), True)

    for i in range(max_iterations):
        z_n = z_n**2 + point_grid
        scappati = np.abs(z_n) >=  2 
        scappati = scappati & Maschera_booleana
        z_i[scappati] = i
        Maschera_booleana[scappati] = False
        z_n[scappati] = np.nan


    return z_i



def main():
    start_timer = time.time()
    #second part
    max_iterations = 200 #good separation from 200 to 500
    v_res = 3000
    h_res = 3000


    mandelbrot_matrix = i_mandelbrot_matrix(h_res, v_res, max_iterations)
    # 1. Creiamo una figura specificando la dimensione in pollici e i DPI.
    # Spiegazione: 40 pollici moltiplicati per 100 DPI generano esattamente 4000 pixel!
    fig = plt.figure(figsize=(30, 30), dpi=100)

    # 2. Diciamo a Matplotlib di occupare TUTTO lo spazio disponibile, eliminando i bordi bianchi
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')  # Spegne gli assi, i numeri e le scritte attorno

    # 3. Mostriamo la matrice (usa .T se necessario come nel tuo codice precedente)
    ax.imshow(mandelbrot_matrix, cmap='magma', origin='lower')

    # 4. SALVATAGGIO REALE: Salva il file direttamente nella cartella del tuo script
    # bbox_inches='tight' e pad_inches=0 eliminano ogni minimo millimetro di bordo rimasto
    plt.savefig("mandelbrot_3k.png", bbox_inches='tight', pad_inches=0)

    # Chiude la figura per liberare istantaneamente la RAM
    plt.close(fig)
    """
    # Sostituisci 'matrice_colori' con il nome della tua matrice
    plt.imshow(mandelbrot_matrix, cmap='magma', origin='lower')

    # Aggiunge una barra laterale che mostra la scala dei colori
    plt.colorbar(label='Numero di iterazioni')

    # Mostra la finestra con il disegno finale
    plt.show()"""
    end_timer = time.time()
    print(f"Time to execute the script = {((end_timer - start_timer)):.4} seconds")


if __name__ == "__main__":
    main()
