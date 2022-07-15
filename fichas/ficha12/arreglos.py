# Pedir el largo de los vectores
def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('cantidad de elementos (> ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n
#carga de elementos en un arreglo
def read(v):
    n = len(v)
    print('Cargue los elementos del vector: ')
    for i in range(n):
        v[i] = int(input('casilla[' + str(i) + ']: ' ))

# producto de vector por constante
def product(v ,k):
    n = len(v)
    for i in range(n):
        v[i] *= k
# suma vectorial
def add(a,b):
    n = len(a)
    c = n * [0]
    for i in range(n):
        c[i] = a[i] + b[i]
    return c
# producto escalar
def scalar_product(a,b):
    n = len(a)
    sp = 0
    for i in range(n):
        sp += a[i]*b[i]
    return sp
# ordenamiento por seleccion directa
def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
# Busqueda lineal
def linear_search(v,x):
    for i in range(len(v)):
        if x == v[i]:
            return i
    return -1

# Busqueda binaria (tiene que estar ordenado v)
def binary_search(v,x):
    izq, der = 0 , len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else: 
            izq = c + 1
    return -1 
# generar arreglo c ordenado a partir de otros dos ya ordenados

def merge(a,b):
    n , m = len(a) , len(b)
    i = k = j = 0
    t = n + m
    c = t * [0]
    while i < n and j < m:
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    v , pos = b , j
    if i < n:
        v , pos = a, i
    while pos < len(v):
        c[k] = v[pos]
        pos += 1
        k += 1
    return c