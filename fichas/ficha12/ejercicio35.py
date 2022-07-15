# Cargar por teclado dos vectores de tamaño n y obtener y mostrar el vector suma
def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <=inf:
            print('Error se pidio mayor a ', inf, ' ... cargue nuevamente ...')
    return n
def read(v):
    n = len(v)
    print('Cargue los elementos del vector: ')
    for i in range(n):
        v[i] = int(input('casilla[' + str(i) + ']: ' ))
def add(a,b):
    n = len(a)
    c = n * [0]
    for i in range(n):
        c[i] = a[i] + b[i]
    return c
def test():
    n = validate(0)
    a = n * [0]
    b = n * [0]
    print('\nVector a: ')
    read(a)
    print('\nVector b: ')
    read(b)

    c = add(a,b)
    print('\nEl vector suma es: ', c)
test()