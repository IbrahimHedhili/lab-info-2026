import numpy as np
from PIL import Image  # Usiamo Pillow al posto di Matplotlib
import matplotlib.pyplot as plt # Ci serve solo per prendere la palette di colori
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
    risoluzione_estrema = 8000  # 8K!
    max_iterations = 300
    nome_file = "mandelbrot_16k_pillow.png"

    print(f"Calcolo ULTRA-VELOCE con Numba ({risoluzione_estrema}x{risoluzione_estrema})...")
    
    import time
    t_inizio = time.time()
    matrice_colori = calcola_mandelbrot_numba(risoluzione_estrema, max_iterations)
    t_fine = time.time()
    
    print(f"Calcolo completato in {t_fine - t_inizio:.3f} secondi!")
    print("Mappatura colori e salvataggio ottimizzato con Pillow (RAM-safe)...")

    # 1. Normalizziamo la matrice tra 0 e 1 per poter applicare la palette di colori
    matrice_normalizzata = matrice_colori.T / max_iterations

    # 2. Prendiamo la palette 'inferno' (o quella che preferisci) da Matplotlib
    # e trasformiamo la matrice di numeri in una mappa di colori RGB (0-255)
    palette = plt.colormaps['inferno']
    matrice_rgb = (palette(matrice_normalizzata)[:, :, :3] * 255).astype(np.uint8)

    # 3. Salviamo l'immagine direttamente su disco saltando Matplotlib
    img = Image.fromarray(matrice_rgb)
    img.save(nome_file)
    
    print(f"Fatto! Immagine 8K salvata senza crash come: '{nome_file}'")

if __name__ == "__main__":
    main()
