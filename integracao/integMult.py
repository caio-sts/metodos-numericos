import numpy as np

def fXYZ(x, y, z):
    return abs( x*y*z )

def mapaXY(vetHoriz, vetVert, camadaZ):
    M = np.zeros((len(vetHoriz),len(vetVert)) )
    for i in range(0,len(vetVert)):
        for j in range(0, len(vetHoriz)):
            M[i][j] = fXYZ( vetHoriz[j] ,vetVert[len(vetHoriz)-1] - i, camadaZ )
    return M

def Trapezio( Xvet, Fvet ):
    h = ( Xvet[len(Xvet)-1] - Xvet[0] ) / ( len(Fvet) - 1 )
    soma = Fvet[0] + Fvet[ len(Fvet) - 1 ]
    for i in range( 1, len(Fvet) - 1 ):
        soma = soma + 2*Fvet[i]
    soma = soma * h / 2

    return abs(soma)

def integtripla( Xvet, Fvet, Zvet ):
    Z = []
    for k in range(0, len(Zvet)):
        M = mapaXY( Xvet, Fvet, Zvet[k] )
        XY = []
        for i in range( 0, len(Fvet) ):
            linha = Trapezio(Xvet, M[i])
            XY.append(linha)
        Z.append( Trapezio( Fvet, XY ) )
    return Trapezio( Zvet, Z)

Xvet = ( [1, 2] )
Fvet = ( [0, 1] )
Zvet = ( [2, 3] )

print( "O valor da integral tripla eh "+str( integtripla( Xvet, Fvet, Zvet) ) )