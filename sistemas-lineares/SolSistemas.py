import numpy as np

# Ax = B
# Dados matriz A e vetor B, queremos encontrar x

#preencher a matriz A
def MatA(ordem):
    matrizA = np.zeros((ordem, ordem), dtype=np.float)
    for i in range(0,ordem):
        for j in range(0,ordem):
            matrizA[i][j] = input(" Insira o elemento "+str(i)+"_"+str(j) +" da matriz: ")
    return matrizA

#Preencher o vetor B
def VetB(ordem):
    vetorCoef = []
    i=0
    while i<ordem:
        vetorCoef.append(float(input(" Insira o elemento " + str(i) + " do vetor de coeficientes.")))
        i = i+1
    return vetorCoef

def MaximoColuna(ordem, matrizA, coluna):
    valor_max = matrizA[coluna][coluna]
    pos = 0
    for i in range(coluna, ordem):
        if( matrizA[i][coluna] > valor_max):
            pos = i
    return pos
def Aplicacao(ordem,A,B):
    #Organizar os pivots(maiores valor da coluna na diagonal principal)
    for i in range(0, ordem):
        pos = MaximoColuna(ordem, A, i)
        if(pos != 0):
            for j in range(i,ordem):
                aux = A[i][j]
                A[i][j] = A[pos][j]
                A[pos][j] = aux
            aux_vet = B[i]
            B[i] = B[pos]
            B[pos] = aux_vet

    #escalonamento
    for k in range(0,ordem-1):
        m = A[k][k]
        for j in range(k, ordem):
            A[k][j] = A[k][j] / m
        B[k] = B[k] / m

        for i in range(1+k, ordem):
            fator = A[i][k] / A[k][k]
            for j in range (k, ordem):
                A[i][j] = A[i][j]-(fator)*A[k][j]
            B[i] = B[i] - fator*B[k]

    vetorRaiz = np.zeros((ordem), dtype=np.float)

    # Solucionar matriz Triang Superior
    for i in reversed(range(0, ordem)):
        soma = 0
        for j in reversed(range(i, ordem)):
            soma = soma + A[i][j] * vetorRaiz[j]
        vetorRaiz[i] = (B[i] - soma) / A[i][i]
    return vetorRaiz

ordem = int(input(" Informe a ordem do sistema linear. "))

#Matriz A
A = MatA(ordem)
#Vetor B
B = VetB(ordem)

print( "O vetor solucao do sistema eh "+str( Aplicacao(ordem,A,B) ) )



"""""

#Determinando o vetor resíduo
residuo = []
for i in range(0, ordem):
    resultado = 0
    for j in range(0, ordem):
        resultado = resultado + matrizOriginal[i][j]*vetorRaiz[j]
    print(resultado)
    residuo.append( CoefOriginal[i] - resultado )

#Verificando se a solucao é exata com o vetor residuo
for i in range(0, ordem):
    if (residuo[i] != 0):
        print("A solucao nao eh exata")"""