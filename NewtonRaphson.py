import numpy as np
from matplotlib import pyplot as plt

def funcao(x):
    return x**3-7.5*x**2+16.5*x-10

def devfunc(x):
    h = 1e-6
    return ( funcao(x+h)-funcao(x-h) )/ ( 2*h )

def xprox(x):
    return x - funcao(x)/devfunc(x)

def NewtonRaphson(x0,maxIt, tol):
    x = x0
    nit = 0
    erro = abs( ( xprox(x) - x) / ( xprox(x)  ) )

    print("Num_It    x              erro")

    while(erro > tol and nit <= maxIt ):
        x = xprox(x)
        erro = abs(( xprox(x) - x) / xprox(x))
        nit = nit + 1
        print("  "+str(nit)+"      "+str(x)+"     "+str(erro))

    print("\nA raiz é "+str(x)+" com erro aproximado de "+str(erro)+" ocorrendo "+str(nit)+" iterações.")
    return x

def plotagem(x0, raiz):
    y = []
    if raiz < x0:
        x = np.linspace(raiz-1, x0, 100)
    else:
        x = np.linspace(x0, raiz + 1, 100)

    for i in range(0, len(x)):
        y.append( funcao( x[i] ) )

    plt.plot(x, y, "-", label="funcao")
    plt.plot(raiz, 0, "x", label="raiz")
    plt.legend(loc="upper left")
    plt.show()

#valor de x aproximado
x0 = 4.54

#numero maximo de iteracoes
maxIt = 10

#tolerancia
tol = 0.0001

#aplicacao
raiz = NewtonRaphson(x0,maxIt,tol)

#plotagem do grafico
plotagem(x0,raiz)