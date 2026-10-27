import numpy as np
import matplotlib.pyplot as plt
import math


def is_mandelbrot_set(c,N):

    z_n = 0
    for i in range(N):
        z_n = z_n**2 + c
        if abs(z_n) > 2: return False
    return True

def iteration_mandelbrot_set(c,max_iterations):

    z_n = complex(0,0)
    i = 0
    while i < max_iterations:
        z_n = z_n*z_n + c
        i += 1
        if abs(z_n) > 2: break
    return i



def main():
    #test
    print("Searching numbers for mundelbrot set :")
    for a in (range(-1,2)):
        for b in range(-1,2):
            if is_mandelbrot_set(complex(a,b),10):
                print(complex(a,b), " True")
            else :
                print(complex(a,b), " False")

    #second part
    max_iterations = 50
    vertical_res = 2000
    horizontal_res = 2000
    mandelbrot_matrix = np.empty((horizontal_res, vertical_res))
    X = 0
    Y = 0 
    for col in range(horizontal_res):
        for row in range(vertical_res):
            X = (col*2 - horizontal_res)/horizontal_res
            Y = (row*2 - vertical_res)/vertical_res
            if is_mandelbrot_set(complex(X,Y), int(math.sqrt(max_iterations))):
                mandelbrot_matrix[col, row] = iteration_mandelbrot_set(complex(X,Y), max_iterations)

    # Sostituisci 'matrice_colori' con il nome della tua matrice
    plt.imshow(mandelbrot_matrix, cmap='twilight_shifted', origin='lower')

    # Aggiunge una barra laterale che mostra la scala dei colori
    plt.colorbar(label='Numero di iterazioni')

    # Mostra la finestra con il disegno finale
    plt.show()


if __name__ == "__main__":
    main()
