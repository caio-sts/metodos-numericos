import numpy as np

def ElimGauss(matriz, coef):
    A = matriz.copy()
    b = coef.copy()

    for i in range(0, len(coef)):
        for j in range(0, len(coef)):
            if ( i != j) :
                fator = A[j][i]/A[i][i]
                b[j] = b[j] -fator*b[i]
                for k in range(0,len(coef)):
                    A[j][k] = A[j][k] - fator*A[i][k]
    for i in range(0,len(coef)):
        b[i] = b[i] / A[i][i]
        A[i][i] = 1

    return b

A = np.array([ [ 1, 1, 1 ], [ 1, 2, 2 ], [ 2, 1, 3 ] ], dtype=np.float)

b = np.array([ 6, 9, 11], dtype=np.float)

print("As raizes sao "+str(ElimGauss(A, b)))
