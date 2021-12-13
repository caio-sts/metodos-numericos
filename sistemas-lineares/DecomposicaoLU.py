import numpy as np

def decomposicaoLU(a):
    #Cria a identidade para ser a L
    L = np.identity(len(a), dtype = np.float)
    #Controla o salto para os pivôs
    for j in range(0, len(a)-1):
        #Captura cada multiplicador
        for i in range(j+1,len(a)):
            m = -a[i][j]/a[j][j]
            L[i][j] = -m
            #Atualiza o valor das entradas de cada linha
            for coluna in range(0, len(a)):
                a[i][coluna] = a[i][coluna] + m*a[j][coluna]
    U = a.copy()

    return L, U

def SolTriangInfer(matriz, coef):
    y = []
    for i in range(0,len(matriz)):
        soma = 0
        for j in range(0,i):
            soma = soma + y[j]*matriz[i][j]
        y.append(coef[i]-soma)

    return y

def SolTriangSuper(matriz, coef):
    x = np.zeros((len(matriz)), dtype = np.float)
    for i in reversed(range(0, len(matriz))):
        soma = 0
        for j in reversed(range(i, len(matriz))):
            soma = soma + matriz[i][j]*x[j]
        x[i] = (coef[i]- soma)/matriz[i][i]

    return x

A = np.array(( [ [ 1, 1, 1 ], [1, 2, 2], [2, 1, 3] ] ), dtype=np.float)
B = [6,9,11]

#Decompor a matriz A em Lower e Upper
L, U = decomposicaoLU(A)

#Resolver o sistema Ly = B
y = SolTriangInfer(L, B)

#O vetor de solucoes x surge ao resolver o sistema linear Ux = y
print("O vetor solucao eh "+str(SolTriangSuper(U, y)))