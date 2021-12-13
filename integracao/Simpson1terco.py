import numpy as np

#n = qntd de intervalos
def f(Xvet, n):
    k = np.linspace( Xvet[0], Xvet[ len(Xvet) - 1 ], n+1)
    y = []
    for x in k:
        # preencha o vetor de y com a funcao
        valor = abs( np.exp(-x) )
        y.append( valor )
    return y

def Simpson1terco(Xvet, Fvet):
    h = ( Xvet[len(Xvet)-1] - Xvet[0] ) / (len(Fvet) - 1 )

    soma = Fvet[0] + Fvet[ len(Fvet) - 1 ]
    for i in range( 1, len(Fvet)-1):
        if ( i%2 == 1 ):
            soma = soma + 4*Fvet[i]
        else:
            soma = soma + 2*Fvet[i]

    return  h*soma/3

def derivadaF(Xvet,n):
    k = np.linspace(Xvet[0], Xvet[len(Xvet) - 1], n + 1)
    y = []
    for x in k:
        # preencha o vetor de y com a funcao derivada
        valor =  -1*np.exp(-x)
        y.append(round(valor, 6))
    return y

def erro (Xvet, FvetDev, m ):
    h = ( Xvet[ len(Xvet) - 1 ] - Xvet[0] ) / m

    derivada = Simpson1terco( Xvet, FvetDev )/ ( Xvet[ len(Xvet) - 1 ] - Xvet[0] )

    derivada = round( derivada  , 3)
    erro = -(m*derivada * h**5)/(180)
    return abs(erro)

def erroSimpson1terco(Xvet,n):
    k = np.linspace(Xvet[0], Xvet[len(Xvet) - 1], n + 1)
    h = ( Xvet[len(Xvet)-1] - Xvet[0] )
    maior = 0
    for x in k:
        #quarta derivada
        if abs(np.exp(-x)) > maior :
            maior = abs(np.exp(-x))

    return (h**5) * maior / ( 2880 * n**4 )

Xvet = [ 1, 2 ]

#criar o vetor f(x) com a quantidade de subintervalos colocada
numSubinterval = 4
Fvet = f(Xvet, numSubinterval)

print( " O valor da integral eh "+str( Simpson1terco(Xvet,Fvet) ) )

#Erro associado ao metodo
print(" A estimativa para o erro associado ao metodo do Trapezio eh " +str( erroSimpson1terco(Xvet,numSubinterval) ) )