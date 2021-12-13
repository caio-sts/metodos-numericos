import numpy as np
from matplotlib import pyplot as plt

def phixr(xr):
    return (float)( 10 / ( xr**2 -7.5*xr+16.5 ) )

def PontoFixo(x0,maxIt,tol):
    xr = x0
    nit = 0

    erro = abs((float)((phixr(xr) - xr) / phixr(xr)))
    print("Num_It      xr                   phixr                    erro")
    print( str(nit) +"            "+str(xr)+ "        "+str(phixr(xr))+"     "+str(erro))
    while (erro >= tol and nit < maxIt):
        xr = phixr(xr)
        erro = abs((float)((phixr(xr) - xr) / phixr(xr)))
        nit = nit + 1

        print(str(nit) + "         " + str(xr)+ "     "+str(phixr(xr)) + "     " + str(erro))
    print("\nA raiz é "+str(phixr(xr))+" com erro igual a "+str(erro)+", ocorrendo "+str(nit)+" iterações.")
    return phixr(xr)

def plotagem(x0, raiz):
    y = []
    if raiz < x0:
        x = np.linspace(raiz-1, x0, 100)
    else:
        x = np.linspace(x0, raiz + 1, 100)

    for i in range(0, len(x)):
        y.append(phixr(x[i]))

    plt.plot(x, y, "-", label="funcao")
    plt.plot(raiz, 0, "x", label="raiz")
    plt.legend(loc="upper left")
    plt.show()
#valor de x aproximado
x0 = 3.8

#numero maximo de iteracoes
maxIt = 10

#tolerancia
tol = 0.001

#aplicacao
raiz = PontoFixo(x0,maxIt,tol)

#plotagem do grafico
plotagem(x0, raiz)