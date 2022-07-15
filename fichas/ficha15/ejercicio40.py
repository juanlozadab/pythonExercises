# Desarrollar un programa que permita cargar por teclado dos arreglos de
# números enteros de n y m componentes respectivamente, y genere y muestre un tercer
# arreglo que contenga los valores que aparecen repetidos en los dos arreglos originales. Es
# decir, el nuevo arreglo debe contener todos los números que estando en uno de los dos
# arreglos originales, están también el otro. Si un número está dos o más veces en el mismo
# arreglo (y también figura en el segundo arreglo), sólo debe aparecer una vez en el tercer
# arreglo.

import functions

def test():
    
    n =functions.validate(0)
    v1 = n * [0]
    functions.read(v1)
    print()

    m = functions.validate(0)
    v2 = m * [0]
    functions.read(v2)
    print()

    v3 = functions.generate(v1,v2)
    print('Los valores presentes en ambos arreglos son: ')
    print(v3)    

test()