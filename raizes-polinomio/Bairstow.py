import numpy as np
import cmath
from matplotlib import pyplot as plt


'''
   Metodo de Bairstow
      r = chute inicial 1
      s = chute inicial 2
      raizes = vetor de raizes
      a = vetor de coeficientes
      grau = grau do polinomio   
'''

#Forma de um número complexo z
def complexo(z):
    if z.imag != 0:
      return round(z.real,6)+round(z.imag,6)*1j
    else:
      return round(z.real,6)

#Método de Bairstow
def bairstow(a,r,s,grau,raizes):
  if(grau<1):
    return None
  if(grau==1):
    raizes.append(float(-a[0])/float(a[1]))
    return None

  if(grau==2):
    D = ((a[1]**2)-((4)*(a[2])*(a[0])))
    X1 = (-a[1] - cmath.sqrt(D))/(2.0*a[2])
    X2 = (-a[1] + cmath.sqrt(D))/(2.0*a[2])
    raizes.append(X1)
    raizes.append(X2)
    return None

  #Criar vetores com o mesmo tamanho do vetores de coeficientes
  n = len(a)
  b = [0]*len(a)
  c = [0]*len(a)

  # Determinar os coeficientes para o cálculo de recorrencia para tornar zero o resto decorrente da divisão do
  # polinomio pelo termo quadrático
  b[n-1] = a[n-1]
  b[n-2] = a[n-2] + r*b[n-1]
  i = n - 3

  while(i>=0):
    b[i] = a[i] + r*b[i+1] + s*b[i+2]
    i = i - 1
  c[n-1] = b[n-1]
  c[n-2] = b[n-2] + r*c[n-1]
  i = n - 3
  while(i>=0):
    c[i] = b[i] + r*c[i+1] + s*c[i+2]
    i = i - 1

  #Resolvendo o sistema linear para encontrar o ajuste de r e s
  r0 = r
  s0 = s
  D = ((c[2]*c[2])-(c[3]*c[1]))**(-1)
  r = r + (D)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
  s = s + (D)*((-c[1])*(-b[1])+(c[2])*(-b[0]))

  tol = 0.001
  #Aplicar o Método de Bairstow recursivamente
  if(abs(b[0])>tol or abs(b[1])>tol):
     return bairstow(a,r,s,grau,raizes)

  #Se o grau do polinômio tem grau >= 3, dividimos o polinomio por x²-rx-s
  if (grau>=3):
    Dis = ((-r)**(2))-((4)*(1)*(-s))
    X1 = (r - (cmath.sqrt(Dis)))/(2.0)
    X2 = (r + (cmath.sqrt(Dis)))/(2.0)
    raizes.append(X1)
    raizes.append(X2)
    return bairstow(b[2:],r,s,grau-2,raizes)

#Determinar o raio da regiao circular onde tem as raízes
def raioRegCircular(grau,a):
  i = 0
  raios = []
  while i <= grau:
      razao = abs(a[i])/abs(a[0])
      raios.append(1+razao)
      i = i + 1
  return max(raios)

def Aplicacao():
  #Instanciação dos vetores e determinação do grau do polinômio
  raizes = []
  a = []
  grau = int(input("Qual o grau do polinomio ? "))

  #Colocacao dos coeficientes do polinomio no vetor
  for k in range(0,grau+1):
      A = float(input("Coef. X^"+str(grau-k)+" ? : "))
      a.append(A)

  raios = raioRegCircular(grau,a)
  print("\nTodas as raizes estão dentro de um disco centrado na origem com raio " + str(raios))

  #Atribuindo um valor para r e s
  r = -raios
  s = raios

  a.reverse()
  bairstow(a,r,s,grau,raizes)
  return a, grau, raizes

def minMaxRaizes(raizes):
  menor = abs(raizes[0])
  maior = abs(raizes[0])
  for i in range(1,len(raizes)):
    if abs(raizes[i]) < menor :
      menor = abs(raizes[i])
    if abs(raizes[i]) > maior:
      maior = abs(raizes[i])
  return menor, maior

def plotagem(a, raizes):
  menor , maior = minMaxRaizes(raizes)

  x = np.linspace(menor - 0.5 ,maior + 0.5, 50)
  y = []
  a.reverse()

  for i in range(0, len(x)):
    valor = 0
    for j in range(0, len(a)):
      valor += a[j] * (pow(x[i], ( len(a) - j - 1 ) ) )
    y.append(valor)

  # Print das raízes
  k = 1
  print("\nRaizes encontradas => ")
  for r in raizes:
    print("Raiz " + str(k) + " = " + str(complexo(r)))
    k += 1

  plt.plot(x, y, "-", label="Polinomio")
  for i in range(0,len(raizes)):
    plt.plot(abs(raizes[i]), 0, "x", label="raiz "+str(i+1))
  plt.legend(loc="upper left")
  plt.show()

#Aplicacao
a, grau, raizes = Aplicacao()

#Plotagem
plotagem(a, raizes)



"""
#Variações de sinal
v=0
a.reverse()
for i in range(0,grau):
    if(a[i]==0 and a[i+1]<0):
      v=v+1
    elif(a[i]<0 and a[i+1]==0 ):
      v=v+1
    elif (a[i]*a[i+1]<0):
      v=v+1
print("\nO numero de variacoes de sinal eh: "+str(v))
a.reverse()
#Possiveis quantidades de raizes positivas
p = []
par=0
while ( v >= par ):
      p.append( v-par )
      par=par+2
print("As possiveis quantidades de raizes positivas sao " +str(p))

#Analisando os coeficientes de p(-x)

coef = a.copy()
i=0
if(grau%2==0):
  while ( i < grau+1 ):
    coef[i] = -1*coef[i]
    i=i+2
else:
  coef.reverse()
  while ( i < grau+1 ):
    coef[i] = -1*coef[i]
    i=i+2

v=0
for i in range(0,grau):
  if (coef[i] == 0 and coef[i + 1] < 0):
    v = v + 1
  elif (coef[i] < 0 and coef[i + 1] == 0):
    v = v + 1
  elif (coef[i]*coef[i+1]<0):
    v=v+1

print("\nO numero de variacoes de sinal em p(-x) eh: "+str(v))


#Possiveis quantidades de raizes negativas
neg = []

par=0
while ( v >= par ):
      neg.append( v-par )
      par=par+2
print("As possiveis quantidades de raizes negativas sao " +str(neg))

#estimativa de raizes complexas
raizesComplex =  []
for i in range(0, len(p)):
  for j in range(0, len(neg)):
    result = grau - p[i] - neg[j]
    if (result%2 == 0):
      raizesComplex.append(result)
print("\nAs possiveis quantidades de raizes complexas sao "+str(raizesComplex))

#Quantidade de raizes complexas
qtdComplex = 0
for r in raizes:
  if(r.imag != 0):
    qtdComplex = qtdComplex + 1
print("\nA quantidade de raizes complexas eh: "+str(qtdComplex))

#Print das raízes
print("\nRaizes encontradas => ")
for r in raizes:
  print("R" + str(k) + " = " + str(complexo(r)))
  k += 1
"""