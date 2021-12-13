import numpy as np

def ElimGauss(matriz, coef):
    A = matriz.copy()
    b = coef.copy()

    for i in range(0, len(coef)):
        for j in range(i+1, len(coef)):
            if (A[i][i]!= 0):
                fator = A[j][i]/A[i][i]
                b[j] = b[j] -fator*b[i]

                for k in range(0,len(coef)):
                    A[j][k] = A[j][k] - fator*A[i][k]
    return SolTriangSuper(A,b)

def SolTriangSuper(matriz, coef):
    x = np.zeros((len(matriz)), dtype = np.float)
    for i in reversed(range(0, len(matriz))):
        soma = 0
        for j in reversed(range(i, len(matriz))):
            soma = soma + matriz[i][j]*x[j]
        x[i] = (coef[i]- soma)/matriz[i][i]
    return x

A = np.array([ [1,1,1], [1,2,2], [2,1,3] ], dtype=np.float)

B = np.array( [6, 9, 11], dtype=np.float)

print("O vetor solucao do sistema é "+str( ElimGauss(A,B) ) )