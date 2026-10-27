import numpy as np
import matplotlib.pyplot as plt

def genera_mandelbrot_ottimizzato(risoluzione, max_iter):
    # 1. Definiamo i confini ottimali per non sprecare spazio vuoto
    x_min, x_max = -2.0, 0.5
    y_min, y_max = -1.25, 1.25

    # 2. Creiamo vettori 1D per le coordinate (occupano pochissimi Kilobyte)
    asse_x = np.linspace(x_min, x_max, risoluzione)
    asse_y = np.linspace(y_min, y_max, risoluzione)

    # 3. Creiamo l'UNICA matrice complessa che si evolverà (Z_n)
    # Usiamo il broadcasting [:, None] per fondere X e Y in una matrice 2D al volo
    Z = asse_x + 1j * asse_y[:, None]

    # 4. Creiamo la SECONDA matrice stabile (Il contatore intero per i colori)
    # Usiamo np.ones così contiamo già la prima iterazione completata con successo
    risultati = np.ones_like(Z, dtype=np.int32)

    # 5. Manteniamo il riferimento dei punti iniziali calcolato al volo, 
    # ma silenziamo gli overflow inevitabili per i punti che scappano all'infinito
    C = Z.copy()
    np.seterr(over='ignore', invalid='ignore')

    # 6. IL CICLO VETTORIALE PRINCIPALE (Unico ciclo sui turni)
    for _ in range(2, max_iter):
        # Applichi la formula a tutti i pixel contemporaneamente
        Z = Z**2 + C
        
        # Aggiorni il contatore in-line senza salvare maschere booleane in RAM
        risultati[np.abs(Z) <= 2] += 1

    return risultati

def main():
    # Parametri per un fantastico sfondo 4K nitido
    # Sul tuo Lenovo con Ubuntu girerà in pochissimi secondi
    risoluzione_4k = 4000
    max_iterations = 300
    nome_file = "mandelbrot_4k_ottimizzato.png"

    print(f"Calcolo del set di Mandelbrot ({risoluzione_4k}x{risoluzione_4k})...")
    matrice_colori = genera_mandelbrot_ottimizzato(risoluzione_4k, max_iterations)
    print("Calcolo completato! Salvataggio dell'immagine pura...")

    # ==========================================
    # BLOCCO DI SALVATAGGIO A RISOLUZIONE NATIVA
    # ==========================================
    # 40 pollici * 100 DPI = esattamente 4000 pixel reali
    fig = plt.figure(figsize=(40, 40), dpi=100)
    
    # Rimuoviamo assi, scritte e cornici grigie per avere solo il frattale puro
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    # Visualizziamo la matrice
    # Scegliamo una mappa di colore ad altissimo contrasto (es. 'inferno', 'magma', 'twilight_shifted')
    ax.imshow(matrice_colori, cmap='inferno', origin='lower')

    # Salviamo l'immagine pixel-per-pixel eliminando ogni bordo residuo
    plt.savefig(nome_file, bbox_inches='tight', pad_inches=0)
    
    # Chiudiamo la figura per svuotare istantaneamente la RAM
    plt.close(fig)
    print(f"Fatto! Il file puro in 4K è stato salvato come: '{nome_file}'")

if __name__ == "__main__":
    main()
