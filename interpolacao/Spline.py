import numpy as np
from matplotlib import pyplot as plt

def Spline(Fvet,Xvet,grauSpl):
    if grauSpl == 1 :
        M = np.zeros( (len(Xvet)-1,grauSpl+1 ) )
        for i in range( 0, len(Xvet) - 1 ) :
            M[i][0] = ( Fvet[i+1] - Fvet[i] ) / ( Xvet[i+1] - Xvet[i] )
        for i in range( 0, len(Xvet)-1):
            M[i][1] = Fvet[i] - M[i][0]*Xvet[i]

        return M

    elif grauSpl == 2 :
        M = np.zeros((len(Xvet) - 1, grauSpl + 1))

        for i in range( 0, len(Xvet)-1 ) :
            mat = np.zeros((3,3))
            vet = np.zeros(3)
            for j in range(0,len(mat)-1):
                for k in range(0,len(mat)):
                    mat[j][k] = pow(Xvet[i + j],len(mat)-1-k)
                vet[j] = Fvet[ i + j ]
            mat[2][0] = 2 * Xvet[ i+1 ]
            mat[2][1] = 1
            M[i] = ElimGauss(mat, vet)

        return M

    elif grauSpl == 3 :
        M = np.zeros((len(Xvet) - 1, grauSpl + 1))

        for i in range( 0, len(Xvet)-1 ) :
            mat = np.zeros((4,4))
            vet = np.zeros(4)
            for j in range(0,len(mat)-2):
                for k in range(0,len(mat)):
                    mat[j][k] = pow(Xvet[i + j],len(mat)-1-k)
                vet[j] = Fvet[ i + j ]
            mat[2][0] = 3*Xvet[i+1]**2
            mat[2][1] = 2 * Xvet[ i+1 ]
            mat[2][2] = 1

            mat[3][0] = 6 * Xvet[i + 1]
            mat[3][1] = 2

            M[i] = ElimGauss(mat, vet)

        return M

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

def plotagem(M, Fvet, Xvet):
    y = []
    horiz = []
    for i in range(0, len(Xvet)-1):
        x = np.linspace(Xvet[i], Xvet[i+1], 10)

        for j in range(0, len(x)):
            horiz.append( x[j] )
            if M.shape[1] == 2:
                y.append( M[i][0] * x[j] + M[i][1] )
            elif M.shape[1] == 3:
                y.append(M[i][0] * x[j]**2 + M[i][1] * x[j] + M[i][2])

            elif M.shape[1] == 4:
                y.append(M[i][0] * x[j]**3 + M[i][1] * x[j]**2 + M[i][2]*x[j] + M[i][3])

    plt.plot(horiz, y, '-', label='Polinomio')
    for i in range(0, len(Xvet)):
        plt.plot(Xvet[i], Fvet[i], 'o', label="Ponto " + str(i + 1))
    plt.legend(loc='upper left')
    plt.title("Polinomio Interpolado de grau " + str( M.shape[1] - 1) )
    plt.show()

Fvet = np.array([0, 1, -1, 10])
Xvet = np.array([1, 2, 3, 5])

#Matriz dos coeficientes das splines de acordo com o grau da Spline
grauSpline = 2
M = Spline(Fvet, Xvet, grauSpline)

#plotagem do grafico das splines
plotagem(M, Fvet, Xvet)
