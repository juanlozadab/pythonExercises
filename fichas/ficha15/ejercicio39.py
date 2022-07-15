# Desarrollar un programa que permita cargar un arreglo con las alturas de n
# personas. Determinar la altura media del grupo, e informar cuántas de esas personas tienen
# altura mayor a la media, y cuántas tienen altura menor o igual a la media.

import functions

def test():
    n = functions.validate(0)
    alt = n * [0]
    functions.read_alt(alt)
    avg = functions.avarage(alt)
    higher_avg , lower_avg= functions.count(alt,avg)
    
    print('La altura media del grupo es: ', avg)
    print('Alturas mayores a la media: ', higher_avg)
    print('Alturas menores a la media: ', lower_avg)
test()