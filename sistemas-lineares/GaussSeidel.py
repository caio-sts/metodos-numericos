import numpy as np

def GaussSeidel( A, B, x0,tol, maxIt ):
    nit = 0
    erro = 1000
    x = x0

    print("nit    x(k)            erro")
    #Iterar preenchimento
    while ( erro>tol and nit < maxIt ):
        xAnt = x.copy()
        #Preencher o vetor x
        for i in range(0, len(A)):
            soma = B[i]
            for j in range(0, len(A)):
                if (i != j ):
                    soma = soma - A[i][j]*x[j]
            soma = soma/A[i][i]
            x[i] = (round(soma,4))

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
def maior(x):
    maior = abs(x[0])
    for i in range(1,len(A)):
        if (abs(x[i]) > maior) :
            maior = abs(x[i])
    return maior

def verifySassenfeld(A):
    Betas = np.zeros(len(A), dtype=np.float)

    for j in range(1, len(A)):
        Betas[0] = Betas[0] + abs(A[0][j])
    Betas[0] = Betas[0]/abs(A[0][0])

    for i in range(1,len(A)):
        Betas[i] = 0
        for j in range(0, i):
            Betas[i] = Betas[i] + abs(A[i][j])*Betas[j]
        for j in range(i+1,len(A)):
            Betas[i] = Betas[i] + abs(A[i][j])
        Betas[i] = Betas[i]/abs(A[i][i])

    Beta = maior(Betas)

    if (Beta < 1) :
        print("(Sassenfeld) O metodo de Gauss-Seidel convergirá!")
    else:
        print("(Sassenfeld) Não há garantia que o método de Gauss-Seidel convergirá!")


A = np.array(( [ 1, 1, 1 ], [ 1, 2, 2 ], [ 2, 1, 3 ]), dtype = np.float)
B = [ 6, 9, 11 ]

#vetor de solucao inicial(palpite)
x0 = [0, 0, 0]

#tolerancia
tol = 0.005

#numero maximo de iteracoes
maxIt = 15

#criterios de convergencia
verifyEstritDominante(A)

verifySassenfeld(A)

#vetor de solucoes
print("Solucoes: "+str(GaussSeidel(A,B, x0,0.005,15)))
