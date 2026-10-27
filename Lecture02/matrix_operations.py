import numpy as np

def main():
    matrix2x2 = np.zeros((2,2))
    print("matrix 2x2: ", matrix2x2)

    # matrix[row, column]
    matrix2x2[1,1] = 1   
    matrix2x2[0,1] = np.nan 
    matrix2x2[0,0] = 3
    matrix2x2[1,0] = 4
    print("matrix 2x2 modified: ", matrix2x2)

    matrix2x2 = matrix2x2**2
    print("matrix 2x2 ^2: ", matrix2x2)

    matrix_false = np.full((2,2), False)
    matrix_true = np.full((2,2), True)
    print("matrix_false : ", matrix_false)
    print("matrix2x2 >= 10 : ", matrix2x2 >= 10)
    maschera_booleana = matrix2x2 >= 10 
    maschera_booleana = maschera_booleana & matrix_true
    print("maschera_booleana: ", maschera_booleana)

    matrix2x2[maschera_booleana] = 0
    print("matrix2x2[maschera_booleana]", matrix2x2)


    #matrix 5x5
    matrix5x5 = np.ones((5,5))
    matrix5x5_true = np.full((5,5),True)
    print("matrix 5x5: ", matrix5x5)
    print("matrix 5x5 True: ", matrix5x5_true)

    matrix5x5 += 1
    print("matrix5x5 += 1 : ", matrix5x5)

    matrix5x5[:,1] = 0
    print("matrix5x5[:,1] = 0: ", matrix5x5)

    n_rows, n_columns = matrix5x5.shape
    print("n_rows = ", n_rows,"\nn_columns = ", n_columns)
    for r in range(n_rows):
        for c in range(n_columns):
            matrix5x5[r, c] = r*c
    print("matrix5x5 : ", matrix5x5)

    scappati = np.abs(matrix5x5) >=  2 
    scappati = scappati & matrix5x5_true
    matrix5x5[scappati] = np.nan
    print("matrix5x5: \n", matrix5x5)


if __name__ == "__main__":
    main()