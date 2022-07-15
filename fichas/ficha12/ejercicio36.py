# Cargar por teclado dos vectores de tamaño n y obtener el producto escalar
# de ambos.

import arreglos

def test():
    n = arreglos.validate(0)
    a = n * [0]
    b = n * [0]

    arreglos.read(a)
    arreglos.read(b)

    pe = arreglos.scalar_product(a, b)
    print('El producto escalar es: ', pe)
test()