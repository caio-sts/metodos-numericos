import numpy as np
from matplotlib import pyplot as plt

def  polinom(dif, xs,x):
    resultado = dif[0]
    erro = dif[len(dif)-1]*( x-xs[0] )

    for i in range(1, len(xs)):
        prod = 1
        erro = erro * ( x - xs[i] )
        for j in range(0,i):
            prod = prod*( x-xs[j] )
        resultado = resultado + dif[i]*prod

    #print("O erro associado a interpolação eh "+str(abs(erro)))
    return resultado

#criar a matriz dos operadores diferença de Newton
def operadoresDif(Fvet, xs):
    num = np.zeros( (len(Fvet),len(Fvet) ) )
    #preencher coluna da matriz com os f(x) conhecidos
    for i in range(0,len(Fvet)):
        num[i][0] = Fvet[i]

    #calcular o restante dos operadores diferenca
    for i in range(1, len(Fvet)):
        for j in range(0, len(Fvet) - i):
                num[j][i] = ( num[j+1][i-1] - num[j][i-1] ) / ( xs[i+j] - xs[j] )

    return num[0]

def plotagem(coefs,Fvet, Xvet):
    x = np.linspace(Xvet[0], Xvet[len(Xvet) - 1], 50)
    y = []

    for i in range(0, len(x)):
        y.append( polinom( coefs, Xvet, x[i] ) )

    plt.plot(x, y, '-', label='Polinomio')
    for i in range(0, len(Xvet)):
        plt.plot(Xvet[i], Fvet[i], 'o', label="Ponto " + str(i + 1))
    plt.legend(loc='upper left')
    plt.title("Polinomio Interpolado de grau " + str(len(Xvet) - 1))
    plt.show()

Fvet = [ 0, 1, -1, 10 ]
Xvet = [ 1, 2, 3, 5 ]

coefs = operadoresDif(Fvet,Xvet)
x = 1
print("O valor do polin. interpolador de Newton no ponto "+str(x)+" eh "+str( polinom(coefs, Xvet, x) ))

#plotagem do polinomio interpolador de newton
plotagem(coefs, Fvet, Xvet)