# Cargar por teclado un arreglo de longitud n, y determinar si los elementos
# del mismo están en secuencia de k en k, siendo k un número que se ingresa también por
# teclado. Por ejemplo:

# v = [2, 5, 8, 11, 14] está en secuencia de 3 en 3 (k = 3)
# v = [4, 6, 8, 10] está en secuencia de 2 en 2 (k = 2)

import functions

def test():
    n = functions.validate(0)
    v = n * [0]
    functions.read(v)
    k = functions.validate(0)
    ok = functions.sequence(v,k)
    if ok:
        print('El arreglo esta en secuencia de ', k , ' en ',k)
    else:
        print('El arreglo no esta en secuencia de ', k , ' en ',k)
test()