import numpy as np

def f(x):
    return np.exp(-x**2)

def integral0aInf(f):
    b = 1

    #integral de 0 a b
    I1 = ( b / 2 ) * ( f(0) + f(b) )

    #integral de b até infinito
    I2 = f(b)
    return abs(I1+I2)

print("O valor da integral eh "+str( integral0aInf(f) ) )
print((np.sqrt( np.pi ))/2)