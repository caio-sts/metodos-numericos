import numpy as np

#n = qntd de intervalos
def f(Xvet, n):
    k = np.linspace( Xvet[0], Xvet[ len(Xvet) - 1 ], n+1)
    y = []
    for x in k:
        # preencha o vetor de y com a funcao
        valor = abs( np.exp(-x) )
        y.append( round( valor, 6) )

    return y

def Simpson3oitavos(Xvet, Fvet):
    h = ( Xvet[len(Xvet)-1] - Xvet[0] ) /  ( len(Fvet) -1 )

    soma = Fvet[0] + Fvet[ len(Fvet) - 1 ]
    for i in range( 1, len(Fvet)-1):
        if i%3 == 0 :
            soma = soma + 2 * Fvet[i]
        else:
            soma = soma + 3 * Fvet[i]

    return  (3 * h * soma) / 8

def erroSimpson3oitavos(Xvet,n):
    k = np.linspace(Xvet[0], Xvet[len(Xvet) - 1], n + 1)
    h = ( Xvet[len(Xvet)-1] - Xvet[0] )
    maior = 0
    for x in k:
        #quarta derivada
        if abs(np.exp(-x)) > maior :
            maior = abs(np.exp(-x))

    return (h**5) * maior / ( 6480 * n**4 )

Xvet = [ 1, 2 ]

#criar o vetor f(x) com a quantidade de subintervalos colocada
numSubinterval = 3
y = f( Xvet, 3 )

print( " O valor da integral eh "+str( Simpson3oitavos( Xvet, y ) ) )

print( " O valor do erro associado eh "+str( erroSimpson3oitavos( Xvet, numSubinterval) ) )