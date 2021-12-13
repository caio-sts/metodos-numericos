import numpy as np

def f(x, y):
    return abs(np.exp(-x)*np.exp(-y))


#Formar a matriz M de acordo com a funcao e os limites
def mapeamentoInteg(Xvet, Fvet):
    M = np.zeros((len(Xvet),len(Fvet)) )
    for i in range(0,len(Fvet)):
        for j in range(0, len(Xvet)):
            M[i][j] = f( Xvet[j] ,Fvet[len(Fvet)-1] - i  )
    return M

def Trapezio(Xvet, Fvet):
    h = ( Xvet[len(Xvet)-1] - Xvet[0] ) / ( len(Fvet) - 1 )
    soma = Fvet[0] + Fvet[ len(Fvet)-1 ]
    for i in range( 1, len(Fvet) - 1 ):
        soma = soma + 2*Fvet[i]
    soma = soma * h / 2

    return abs(soma)

def integdupla( x, y, T ):
    XY = []
    for i in range(0,len(y)):
        linha = Trapezio( x, T[i] )
        XY.append( linha )

    return Trapezio(y,XY)

#Atencao em como se quer integrar, separar em varios pontos ou só com os limites de integraca
Xvet = np.array([ 1, 2 ] )
Fvet = np.array( [ 0, 1 ] )

#Caso se queira usar uma matriz com os valores adequados a cada x e y
M = np.array( [ [np.exp(-2), np.exp(-3) ], [ np.exp(-1), np.exp(-2) ] ] )

#Caso, de acordo com a funcao de duas variáveis, queira montar a matriz que mapeia os valores
M1 = mapeamentoInteg(Xvet,Fvet)

print("O valor da integral dupla eh "+str( integdupla(Xvet,Fvet,M1) ))