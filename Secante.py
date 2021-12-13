import numpy as np
from matplotlib import pyplot as plt

def funcao(x):
    return x**3-7.5*x**2+16.5*x-10

def Secante(x0,x1,tol,maxIt):
    nit = 0
    xprox = ( x0*funcao(x1) - x1*funcao(x0) ) / (funcao(x1) - funcao(x0))
    erro = abs((x1 - x0) / x1)
    print("Num_It    x                    erro")

    while( erro >= tol and nit <= maxIt ):
        xprox = ( x0*funcao(x1) - x1*funcao(x0)) / (funcao(x1)-funcao(x0))
        x0 = x1
        x1 = xprox
        erro = abs((x1 - x0) / x1)
        nit = nit + 1
        print("  "+str(nit)+"      "+str(xprox)+"     "+str(erro))

    print("\nA raiz é "+str(xprox)+" com erro aproximado de "+str(erro)+" ocorrendo "+str(nit)+" iterações.")
    return xprox

def plotagem(a, b, raiz):
    y = []
    x = np.linspace(a, b, 100)
    for i in range(0, len(x)):
        y.append(funcao(x[i]))

    plt.plot(x, y, "-", label="funcao")
    plt.plot(raiz, 0, "x", label="raiz")
    plt.legend(loc="upper left")
    plt.show()

#intervalo de interesse
x0 = 3.5
x1 = 4.5

#numero maximo de iteracoes
maxIt = 10

#tolerancia
tol = 0.001

#aplicacao
raiz = Secante(x0,x1,tol,maxIt)

#plotagem do grafico
plotagem( x0, x1, raiz)