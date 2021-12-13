import numpy as np

def salvaCol(matrizA,j):
    col = []
    for i in range(0,len(matrizA)):
        col.append(matrizA[i][j])
    return col

def Cramer (matrizA, tind ):
    M = matrizA.copy()
    b = tind.copy()
    D = np.linalg.det(M)
    if (D != 0):
        x = np.ones(len(b), dtype=np.float)
        for i in range(0,len(b)):
            Col = salvaCol(M, i)
            Di = A
            for j in range(0, len(b)):
                Di[j][i] = b[j]
            detDn = np.linalg.det(Di)
            x[i] = ( detDn/D )

            #recuperar as entradas da respectiva coluna
            for k in range(0,len(b)):
                A[k][i] = Col[k]

    else:
        print("O determinante da matriz é 0, ou seja, o sistema correspondente é indeterminado ou impossivel.")
        return None

    return x

A = [ [1,1,1], [1,2,2], [2,1,3] ]
B = [6, 9, 11]

print("As solucoes sao: "+str(Cramer(A,B)))