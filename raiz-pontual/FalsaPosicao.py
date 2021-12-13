import numpy as np
from matplotlib import pyplot as plt

def funcao(x):
    return x**3-7.5*x**2+16.5*x-10

def FalsaPosicao(a,b,E,maxIt):
    xAnt = 0
    Num_it = 0
    erro = 1
    if( (funcao(a) * funcao(b)) < 0 ):

        x = (b*funcao(a) - a*funcao(b))/(funcao(a)-funcao(b))

        erro = abs((float)((x-xAnt)/x))
        print("Num_it, xAnt,     erro ")
        while( erro > E and Num_it <= maxIt):
            Num_it = Num_it + 1
            if( funcao(a)*funcao(x) < 0 ):
                b = x
                x = (b*funcao(a)- a*funcao(b))/(funcao(a)-funcao(b))
                xAnt = b
                erro = abs((float)((x-xAnt)/x))
                print("  "+str(Num_it)+"     "+str(xAnt)+"       "+str(erro))

            elif( funcao(x) * funcao(b) < 0 ) :
                a=x
                x = (b*funcao(a)- a*funcao(b))/(funcao(a) - funcao(b))
                xAnt =a
                erro = abs((float)((x-xAnt)/x))
                print("  "+str(Num_it)+"     "+str(xAnt)+"      "+str(erro))

            else:
                erro = 0
                xAnt = x
                print("  " + str(Num_it) + "     " + str(xAnt) + "     " + str(erro))
                break
    print("\n A raiz do intervalo é "+str(xAnt)+" e o erro é "+str(erro)+" ocorrendo "+str(Num_it)+" iterações.")
    return xAnt

def plotagem(a, b, raiz):
    y = []
    x = np.linspace(a, b, 100)
    for i in range(0, len(x)):
        y.append(funcao( x[i] ) )

    plt.plot(x, y, "-", label="funcao")
    plt.plot(raiz, 0, "x", label="raiz")
    plt.legend(loc="upper left")
    plt.show()

#intervalo de interesse
a = 3.5
b = 4.5

#tolerancia
tol = 0.01

#numero maximo de iteracoes
maxIt = 10

#aplicacao
raiz = FalsaPosicao(a, b, tol, maxIt)

#plotagem do grafico
plotagem(a, b, raiz)