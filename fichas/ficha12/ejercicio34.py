# cargar por teclado un arreglo de n componentes y multiplicarlo por el valor k que tambien se ingresa por teclado
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
    

def product(v ,k):
    n = len(v)
    for i in range(n):
        v[i] *= k
    

def test():
    n = validate(0)
    # crear un arreglo de n elementos, valor inicial 0
    v = n * [0]
    read(v)
    k = int(input('Ingrese el valor de k: '))
    product(v,k)
    print('el vector quedo asi: ', v)


test()