# Desarrollar un programa controlado por menu de opciones, que incluya opciones para realizar:
# 1 - Cargar un valor n entero por teclado, validadando que sea mayor a cero, y mostrar 
#     todos los numeros impares y multiplos de 3 que haya en el intervalo [1,n]
# 2 - Cargar dos valores a y b por teclado, validando que 1 < a < b y determinar si existe algun
#     numero primo en el intervalo [a,b], si existe, muestrelo
# 3 - Cargar por teclado una secuencia de numeros uno  a uno, cortando cuando sea cero, determinar si 
#     todos los numeros entraron ordenados de menor a mayor


def menu():
    print('Menu de opciones y funciones generalizadas')
    op = 1
    while op != 4:
        print('1 - Inpares multiplos de 3')
        print('2 - Primos en un intervalo')
        print('3 - Secuencia ordenada')
        print('4 - Salir')
        op = int(input('Ingrese el numero de la opcion elegida: '))

        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
        elif op == 4:
            break

        
def opcion1():
    n = validar_mayor_que(0)
    res = odd_multiples(n)
    print('Intervalo analizado: [ 1 ,', n ,']')
    print('Impares multiplos de 3 en ese intervalo: ', res)

def opcion2():
    a = validar_mayor_que(1)
    b = validar_mayor_que(a)
    primo = search_prime(a,b)
    print(primo)
    print('Intervalo analizado: [',a,',',b,'] ')
    if primo is not None:
        print('el primer primo encontrado en ese intervalo es: ', primo)
    else:
        print('No hay numeros primos en ese intervalo')

def opcion3():
    ok = check_order()
    if ok:
        print('la secuencia esta ordenada de menor a mayor')
    else:
        print('la secuencia no esta ordenada de menor a mayor')

def validar_mayor_que(inf):
    n = inf - 1
    while n <= inf:
        n = int(input('valor (>' + str(inf) + ' por favor... : '))
        if n <= inf:
            print('error se pidio >' + str(inf) , 'cargue de nuevo')
    return n

def odd_multiples(n):
    r = ()
    for i in range(3, n+1, 6):
        r += i,
    return r

def search_prime(a ,b):
    p = next_prime(a-1)
    if p <= b:
        return p
    return None
    
def next_prime(n):
    if n < 2:
        return 2
    p = n + 1
    if p % 2 == 0:
        p += 1
    while not is_prime(p):
        p += 2
    return p

def is_prime(n):
    if n < 0:
        return None
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    raiz = int(pow(n, 0.5))
    for div in range(3,raiz+1,2):
        if n % div == 0:
            return False
    return True

def check_order():
    ok = True
    num = int(input('Cargue el primer valor (con 0 corta): '))
    anterior = num
    while num != 0:
        if num < anterior: 
            ok = False
        anterior = num
        num = int(input('Ingrese el siguiente valor (con 0 corta): '))
    return ok
menu()