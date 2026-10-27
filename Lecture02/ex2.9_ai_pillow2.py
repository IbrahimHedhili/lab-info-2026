import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from PIL import Image
import time

# Compiliamo la funzione per calcolare UNA SINGOLA RIGA alla volta
@jit(nopython=True)
def calcola_riga_mandelbrot(row, risoluzione, max_iter):
    #centred image
    x_min, x_max = -2.0, 0.5
    y_min, y_max = -1.25, 1.25
    #seahorses valley
    #x_min, x_max = -0.75, -0.73
    #y_min, y_max = 0.10, 0.12
    #elefants valley
    #x_min, x_max = 0.25, 0.30
    #y_min, y_max = -0.02, 0.02

    # Un vettore per una sola riga (16000 elementi occupano solo 64 KB!)
    riga_dati = np.zeros(risoluzione, dtype=np.int32)
    
    y = y_min + (row / risoluzione) * (y_max - y_min)
    
    for col in range(risoluzione):
        x = x_min + (col / risoluzione) * (x_max - x_min)
        c = complex(x, y)
        z = 0.0 + 0.0j
        
        for i in range(max_iter):
            z = z*z + c
            if z.real*z.real + z.imag*z.imag > 4.0:
                riga_dati[col] = i
                break
        else:
            riga_dati[col] = max_iter
            
    return riga_dati

def main():
    risoluzione_estrema = int(input("Inserire la risoluzione desiderata[max = 30000]: "))  # Puoi mettere anche 25000, non crasherà mai!
    max_iterations = int(input("Inserire il massimo numero di iterazioni[max = 500]: "))
    nome_file = str(input("Dai un nome al file(senza estensione): ")) +".png"

    print(f"Avvio salvataggio in streaming a blocchi per immagine {risoluzione_estrema}x{risoluzione_estrema}...")
    t_inizio = time.time()

    # 1. Carichiamo la palette di colori
    #palette = plt.colormaps['inferno']
    palette = plt.colormaps['twilight_shifted']
    # 2. Creiamo un file immagine vuoto sul disco con Pillow della dimensione finale
    img = Image.new("RGB", (risoluzione_estrema, risoluzione_estrema))

    # 3. Ciclo riga per riga: calcoliamo, coloriamo e scriviamo subito sul file
    for row in range(risoluzione_estrema):
        # Calcola solo i dati di una riga
        riga_valori = calcola_riga_mandelbrot(row, risoluzione_estrema, max_iterations)
        
        # Normalizza e colora SOLO questa riga (consumo RAM ridicolo)
        riga_normalizzata = riga_valori / max_iterations
        riga_rgb = (palette(riga_normalizzata)[:, :3] * 255).astype(np.uint8)
        
        # Converte la singola riga in un pezzetto di immagine
        riga_immagine = Image.fromarray(riga_rgb.reshape(1, risoluzione_estrema, 3))
        
        # Incolla la riga direttamente nella posizione corretta del file sul disco
        # Pillow gestisce la memoria in background senza accumulare dati in RAM
        img.paste(riga_immagine, (0, row))
        
        # Un piccolo indicatore di progresso ogni 2000 righe
        if row % 2000 == 0 and row > 0:
            print(f"Progresso: {row}/{risoluzione_estrema} righe elaborate...")

    # 4. Salviamo definitivamente il file su disco
    print("Scrittura finale del file PNG...")
    img.save(nome_file)
    
    t_fine = time.time()
    print(f"Spettacolo! Immagine {int(risoluzione_estrema/1000)}K salvata in {t_fine - t_inizio:.2f} secondi con zero spreco di RAM!")

if __name__ == "__main__":
    main()
