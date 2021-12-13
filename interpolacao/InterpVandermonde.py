import numpy as np
import math
from matplotlib import pyplot as plt
def polinom(coefs,x):
    resultado = 0
    for i in range(0,len(coefs)):
        resultado = resultado + coefs[i]*math.pow(x,i)

    return resultado

def Interpol(xs, fs):
    M = np.zeros(len(xs),len(xs))

    for j in range(0,len(xs)):
        for i in range(0,len(xs)):
            M[i][j] = math.pow(xs[i],j)

    coefs = ElimGauss(M,fs)
    return coefs

def ElimGauss(matriz, coef):
    A = matriz.copy()
    b = coef.copy()

    for i in range(0, len(coef)):
        for j in range(0, len(coef)):
            if ( i != j) :
                fator = A[j][i]/A[i][i]
                b[j] = b[j] -fator*b[i]
                for k in range(0,len(coef)):
                    A[j][k] = A[j][k] - fator*A[i][k]

    for i in range(0,len(coef)):
        b[i] = b[i] / A[i][i]
        A[i][i] = 1

    return b

def plotagem(coefs,Fvet,Xvet):
    x = np.linspace( Xvet[0], Xvet[ len(Xvet) - 1 ], 50 )
    y = []

    for i in range(0,len(x)):
        y.append(polinom(coefs,x[i]))

    plt.plot(x,y,'-', label='Polinomio')
    for i in range(0,len(Xvet)):
        plt.plot( Xvet[i],Fvet[i],'o',label="Ponto "+str(i+1) )
    plt.legend(loc='upper left')
    plt.title("Polinomio Interpolado de grau "+str(len(Xvet)-1))
    plt.show()


Fvet = np.array( [0, 1, -1, 10], dtype=np.float64)
Xvet = np.array( [ 1, 2, 3, 5], dtype=np.float64)

#Tomando os coeficientes interpolados
coefs = Interpol( Xvet, Fvet )

#Print dos coeficientes no console
print( "Os coeficientes interpolados sao: "+str(coefs) )

#plotagem do polinomio interpolado
plotagem(coefs,Fvet,Xvet)
