import numpy as np
import matplotlib.pyplot as plt
from numba import jit, prange

# @jit dice a Numba di compilare la funzione in codice macchina nativo.
# nopython=True attiva la massima velocità (evita il sovraccarico di Python).
# parallel=True dice a Numba di usare TUTTI i core della CPU in parallelo.
@jit(nopython=True, parallel=True)
def calcola_mandelbrot_numba(risoluzione, max_iter):
    x_min, x_max = -2.0, 0.5
    y_min, y_max = -1.25, 1.25
    
    # Creiamo la matrice dei risultati direttamente della dimensione finale
    matrice = np.zeros((risoluzione, risoluzione), dtype=np.int32)
    
    # prange (parallel range) dice a Numba di distribuire i cicli sui vari core della CPU
    for col in prange(risoluzione):
        # Mappatura matematica della X eseguita al volo per ogni colonna
        x = x_min + (col / risoluzione) * (x_max - x_min)
        
        for row in range(risoluzione):
            # Mappatura matematica della Y eseguita al volo per ogni riga
            y = y_min + (row / risoluzione) * (y_max - y_min)
            
            c = complex(x, y)
            z = 0.0 + 0.0j
            
            # Ciclo dei turni tradizionale (grazie al C, il break qui è fulmineo)
            for i in range(max_iter):
                z = z*z + c
                if z.real*z.real + z.imag*z.imag > 4.0: # z.real*z.real + z.imag*z.imag > 4.0 è molto più veloce di abs(z) > 2 perché evita la radice quadrata!
                    matrice[col, row] = i
                    break
            else:
                matrice[col, row] = max_iter
                
    return matrice

def main():
    risoluzione_4k = 16000
    max_iterations = 300
    nome_file = "mandelbrot_16k_numba.png"

    print(f"Calcolo ULTRA-VELOCE del set di Mandelbrot ({risoluzione_4k}x{risoluzione_4k}) con Numba...")
    
    # Avviamo il calcolo
    import time
    t_inizio = time.time()
    matrice_colori = calcola_mandelbrot_numba(risoluzione_4k, max_iterations)
    t_fine = time.time()
    
    print(f"Calcolo completato in appena {t_fine - t_inizio:.3f} secondi!")
    print("Salvataggio dell'immagine pura in corso...")

    # Blocco di salvataggio identico a prima per avere l'immagine nativa in 4K
    fig = plt.figure(figsize=(40, 40), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    # Usiamo la trasposta (.T) per allineare correttamente gli assi X e Y
    ax.imshow(matrice_colori.T, cmap='inferno', origin='lower')

    plt.savefig(nome_file, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    print(f"Immagine salvata con successo come: '{nome_file}'")

if __name__ == "__main__":
    main()
