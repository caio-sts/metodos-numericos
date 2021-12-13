import numpy as np

M = np.array([ [3,-2,5,1], [-6,4,-8,1], [9,-6,19,1],[6,-4,-6,15]], dtype=np.float)

tind = [7,1,4,12]

def elimina_gauss_pivot_parcial(M,tind):
        A = np.array((M), dtype= np.float)
        b = np.array((tind),dtype= np.float)
        nraizes = len(A)
        k=0
        while k<nraizes:
            z=k+1
            idl=0
            while z<nraizes:
                if abs(A[z,k]) > abs(A[k,k]):
                    idl=z
                z=z+1
            if idl !=0:
                j=0
                while j<nraizes:
                    ttemp = A[k,j]
                    A[k,j]=A[idl,j]
                    A[idl,j]=ttemp
                    j=j+1
                ttemp=b[k]
                b[k]=b[idl]
                b[idl]=ttemp
            z=k+1
            while z<nraizes:
                fator=(-1)*A[z,k]/A[k,k]
                j=0
                while j<nraizes:
                    A[z,j]=fator*A[k,j]+A[z,j]
                    j=j+1
                b[z]=fator*b[k]+b[z]
                z=z+1
            k=k+1

        #Divide as linhas pelo pivot
        for k in range(0, len(A) ):
            m = A[k][k]
            for j in range(k, len(A)):
                A[k][j] = A[k][j] / m
            b[k] = b[k] / m
        return A,b

def SolTriangSuper(matriz, coef):
    x = np.zeros((len(matriz)), dtype = np.float)
    for i in reversed(range(0, len(matriz))):
        soma = 0
        for j in reversed(range(i, len(matriz))):
            soma = soma + matriz[i][j]*x[j]
        x[i] = (coef[i]- soma)/matriz[i][i]
    return x

A, b = elimina_gauss_pivot_parcial(M, tind)
x = SolTriangSuper(A,b)

print("As raízes são "+str(x))


