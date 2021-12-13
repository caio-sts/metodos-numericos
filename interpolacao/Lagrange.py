import numpy as np
from matplotlib import pyplot as plt

def polinom(Fvet,Xvet,x):
    coefL = []
    for i in range( 0,len(Fvet) ):
        coefL.append(L(Xvet,x,i))

    resultado = 0
    for i in range(0,len(Fvet)):
        resultado = resultado + Fvet[i]*coefL[i]

    return resultado

def L(Xvet,x,indice):
    num = 1.0
    den = 1.0
    for i in range(0,len(Xvet)):
        if(i != indice):
            num = num*(x-Xvet[i])
            den = den*(Xvet[indice]-Xvet[i])

    return num/den

def plotagem(Fvet, Xvet):
    x = np.linspace(Xvet[0], Xvet[len(Xvet) - 1], 50)
    y = []

    for i in range(0, len(x)):
        y.append( polinom( Fvet, Xvet, x[i] ) )

    plt.plot(x, y, '-', label='Polinomio')
    for i in range(0, len(Xvet)):
        plt.plot(Xvet[i], Fvet[i], 'o', label="Ponto " + str(i + 1))
    plt.legend(loc='upper left')
    plt.title("Polinomio Interpolado de grau " + str(len(Xvet) - 1))
    plt.show()

Fvet = np.array( [0, 1, -1, 10] )
Xvet = np.array( [ 1, 2, 3, 5] )

x = 4
print("\nO valor do polinomio no ponto "+str(x)+" eh "+str(polinom(Fvet,Xvet,x)))

plotagem(Fvet,Xvet)