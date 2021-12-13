import numpy as np

#n = numero de subintervalos
def f(Xvet, n):
    k = np.linspace(Xvet[0], Xvet[ len(Xvet)-1 ], n+1)
    f = []
    for x in k:
        f.append( abs( - x + 2 ) )

    return f

def Trapezio(Xvet, Fvet):
    h = ( Xvet[len(Xvet)-1] - Xvet[0] ) / ( len(Fvet) - 1 )
    soma = Fvet[0] + Fvet[ len(Fvet)-1 ]
    for i in range( 1, len(Fvet) - 1 ):
        soma = soma + 2*Fvet[i]
    soma = soma * h / 2

    return abs(soma)

def erroTrap(Xvet,n):
    k = np.linspace(Xvet[0], Xvet[len(Xvet) - 1], n + 1)
    h = ( Xvet[len(Xvet)-1] - Xvet[0] )
    maior = 0
    for x in k:
        #segunda derivada
        if abs(np.exp(-x)) > maior :
            maior = abs(np.exp(-x))

    return (h**3) * maior / ( 12 * n**2 )

Xvet = np.array( [1, 3] )

#criar o vetor f(x) com a quantidade de subintervalos colocada
numSubinterval = 4
Fvet = f(Xvet, numSubinterval)

print( " O valor da integral pelo metodo do Trapezio eh "+str( Trapezio( Xvet, Fvet ) ) )

#Erro associado ao metodo
print(" A estimativa para o erro associado ao metodo do Trapezio eh " +str( erroTrap(Xvet,numSubinterval) ) )