import numpy as np

def GaussJacobi( A, B, x0,tol, maxIt ):
    C = np.zeros((len(A),len(A)), dtype = np.float)
    nit = 0
    erro = 1000
    x = x0

    #Criando a matriz C ( x(k+1) = C * x(k) + B ) OK
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if(i != j):
                C[i][j] = -A[i][j]/A[i][i]

    print("nit    x(k)            erro")

    #Atualizar os valores do vetor de coef. independentes OK
    for i in range(0,len(A)):
        B[i] = B[i]/A[i][i]

    #Iterar preenchimento
    while ( erro>tol and nit < maxIt ):
        xAnt = x.copy()

        #Preencher o vetor x
        for i in range(0, len(A)):
            soma = B[i]
            for j in range(0, len(A)):
                soma = soma + C[i][j]*xAnt[j]
            x[i] = round(soma,4)

        erro = round((distMaior(xAnt, x)/maior(x)),4)
        nit = nit + 1
        print(nit , x , erro)

    return x

def distMaior(xAnt, x):
    distMax = abs(x[0]-xAnt[0])
    for i in range(1,len(A)):
        if (abs(x[i]-xAnt[i]) > distMax) :
            distMax = abs(x[i]-xAnt[i])
    return distMax

def maior(x):
    maior = abs(x[0])
    for i in range(1,len(A)):
        if (abs(x[i]) > maior) :
            maior = abs(x[i])
    return maior

def verifyEstritDominante(A):
    contador = 0
    for i in range(0,len(A)):
        supostoMaior = abs(A[i][i])
        soma = 0
        for j in range(0,len(A)):
            if ( i != j ):
                soma = soma + abs(A[i][j])
        if (supostoMaior > soma) :
            contador = contador + 1
    if contador == len(A) :
        print("O método convergirá pois a diagonal é estritamente dominante.")
    else:
        print("\nA diagonal não é estritamente dominante")

A = np.array(([10,2,1], [1,5,1], [2,3,10]), dtype = np.float)
B = [ 7, -8, 6]

#vetor solucao inicial(palpite)
x0 = [ 0.7, -1.6, 0.6]

#tolerancia
tol = 0.05

#numero maximo de iteracoes
maxIt = 10

#criterio de convergencia
verifyEstritDominante(A)

#vetor de solucoes
print("\nAs raízes sao "+str(GaussJacobi(A,B,x0,0.05, 3)))