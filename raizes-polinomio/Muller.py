import math
# FALTA IMPLEMENTAR ALTERAÇOES PARA RESOLVER QUADRADOS PERFEITOS, raizes iguais

def f(x):
    y = x**4 -2*x**3 +6*x**2 -8*x+ 8
    return y

def complexo(z):
    x = complex (0, 0)
    if( z.real != 0):
        x = complex( round(z.real, 4), 0)
    else:
        x = complex( 0, 0)

    if( z.imag != 0):
        x = x +  complex (0, round(z.imag , 4) )

    return x.real +x.imag*1j

def muller( x0, x1, x2,nraizes, tol):
    erro = 1000
    raizes = []
    id_raiz = 0
    while (id_raiz < nraizes ):
        while ( erro > tol  ):
            fx0 = f(x0)
            fx1 = f(x1)
            fx2 = f(x2)
            h0 = (x1-x0)
            h1 = (x2-x1)

            d0 = (fx1-fx0)/(x1-x0)
            d1 = (fx2-fx1)/(x2-x1)

            a = ( d1 - d0 )/(x2-x0)
            b = (a*h1) + d1
            c = f(x2)

            if (b.real >= 0):
                dlt = b**2 -4*a*c
                if ( dlt.real >= 0):
                    delta = math.sqrt (dlt.real)
                else:
                    delta = complex ( 0, math.sqrt(-1*dlt.real) )
            elif(b.real <0):
                dlt = (b**2) -4*a*c
                if ( dlt.real >= 0 ):
                    delta = -1* math.sqrt( dlt.real)
                else:
                    delta = complex( 0, -1j*math.sqrt(-1*dlt.real))

            x3 = x2 + ((-2*c) / (b + delta))
            erro = abs((x3-x2)/x3)

            x0=x1
            x1=x2
            x2=x3

        if ( id_raiz > 0 ):
            vbol=0
            for i in range(0,id_raiz):
                if( x3 == raizes[i] ):
                    vbol = 1
            if(vbol==0):
                if (x3.imag != 0):
                    raizes.append(complexo(complex(x3.real, x3.imag)))
                    raizes.append(complexo(complex(x3.real,-1*x3.imag)))
                    id_raiz=id_raiz+2

                else:
                    raizes.append(complexo(complex(x3.real, x3.imag)))
                    id_raiz=id_raiz+1

        else:
            if (x3.imag != 0):
                raizes.append(complexo(complex(x3.real, -1*x3.imag)))
                raizes.append(complexo(complex(x3.real, x3.imag)))
                id_raiz = id_raiz + 2
            else:
                raizes.append(complexo(complex(x3.real, x3.imag)))
                id_raiz = id_raiz + 1

        x0 = x3 - 2
        x1 = x0 + 4
        x2 = x1 - 6
        erro = 1000
    return raizes

print("As raizes sao "+str(muller( -1.5, 0.1, 3, 4, 0.0001) ))



