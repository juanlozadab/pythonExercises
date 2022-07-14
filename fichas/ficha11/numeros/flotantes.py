
def promedio(x1, x2 , *x):
    suma = x1 + x2
    conteo = 2
    n = len(x)
    if(n != 0):
        for i in range(n):
            suma += x[i]
        conteo += n
    return suma / conteo
     