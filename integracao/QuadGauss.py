import numpy as np

def f(x):
    return abs( np.exp(-x) )

def quadGauss2Pontos(Xvet):
    soma =  ( Xvet[len(Xvet)-1] + Xvet[0] ) / 2
    subt = ( Xvet[len(Xvet)-1] - Xvet[0] ) / 2
    return ( subt ) * ( f( soma + subt*(-np.sqrt(3)/3) ) + f( soma + subt*(np.sqrt(3)/3) ) )

def quadGauss3Pontos(Xvet):
    soma =  ( Xvet[len(Xvet)-1] + Xvet[0] ) / 2
    subt = ( Xvet[len(Xvet)-1] - Xvet[0] ) / 2
    return ( subt ) * ( 5*( f( soma + subt * ( -np.sqrt(3) / 3 ) ) + f( soma + subt * ( np.sqrt(3) / 3 ) ) )/9 + 8 * f(soma) / 9 )

Xvet = ([ 1, 2 ])

print(" O valor da integral pela metodo da quadratura de Gauss eh " +str(quadGauss2Pontos(Xvet)))

print(" O valor da integral pela metodo da quadratura de Gauss eh " +str(quadGauss3Pontos(Xvet)))

