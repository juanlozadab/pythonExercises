# Desarrollar un programa controlado por menu de opciones, que incluya tareas para realizar las siguientes tareas:
# 1 - cargar por teclado la cantidad n de colores que pueden tener los automoviles a la venta en una concesionaria
#     ademas de la cantidad m de modelos que existen de un marca en particulas, y finalmente la cantidad t de 
#     opciones que se ofrecen a los clientes en cuanto a tipos de neumaticos a aplicar en cada vehiculo.
#     calcule la cantidad total de combinaciones que tiene un cliente cuando deba elegir un automovil de esa marca.
# 2 - Para el disenio de un juego de tablero basado en combinar n silabas, se desea saber cuantas formas diferentes 
#     existen de combinar esas n silabas, sin repetirlas. cargar n por teclado y mostrar esa cantidad
# 3 - Cargar por teclado la cantidad n de agentes de seguridad disponibles en una compania de servicios de vigilancia.
#     la compania desea que en todo momento, sus agentes se distribuyan en grupos de m agentes. calcule la cantidad
#     de grupos diferentes que pueden formarse.
# 4 - Cargar por teclado la cantidad n de corredores que participan de una carrerar de f1, cargue tambien por teclado 
#     la cantidad m , con m < n , de posiciones finales que tendran puntos por llegar en esas posiciones. calcular y 
#     mostrar la cantidad de posibles formas en que pueden cubrirse las m posiciones puntuables, con los n corredores.
# 5 - Cargar por teclado la cantidad m de letras que conforman la clave de identificacion asignada a los empleados de 
#     una empresa . Sabiendo que las posibles letras diferentes del alfabeto son 27, calcular la cantidad de formas 
#     que podria tener una clave
# 6 - Cargar por teclado la cantidad n de colores que pueden tener las fichas contenidas en una bolsa, y la cantidad
#     m de fichas que se deben extraer de la bolsa para un ejercicio de probabilidades. calcular la cantidad de 
#     variantes que puede tener cada conjunto posible de m fichas en cuanto a sus posibles colores.
def combinaciones_sin_reposicion(n,m):
    fn = factorial(n)
    fm = factorial(m)
    fr = factorial(n - m)
    return fn // (fm * fr)

def combinaciones_con_reposicion(n,m):
    fn = factorial(m + (n - 1))
    fm = factorial(m)
    fr = factorial(n - 1)
    return fn // (fm * fr)

def factorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f
def permutaciones_con_reposicion(n,m):
    return pow(n,m)

def permutaciones_sin_reposicion(n,m):
    fn = factorial(n)
    fd = factorial(n - m)
    return fn // fd

def total_resultados(n,m,t):
    return n * m * t

def validar_mayor_que(inf):
    n = inf - 1
    while n < inf:
        n = int(input('Ingrese valor (mayor que ' + str(inf) + ') por favor: '))
        if n < inf:
            print('Error... se pidio >' + str(inf) , '... cargue de nuevo ...')
        return n

def validar_intervalo(inf,sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor (entre ' + str(inf) + ' y ' + str(sup) + ': '))
        if n < inf or n > sup:
            print('Se pidio entre ', inf , ' y ' ,sup, '... cargue de nuevo...')
    return n

def opcion1():
    print('Candidad de colores...')
    n = validar_mayor_que(0)
    print('Cantidad de modelos...')
    m = validar_mayor_que(0)
    print('Cantidad de tipos de neumaticos...')
    t = validar_mayor_que(0)
    res = total_resultados(n,m,t)
    print('Cantidad total de combinaciones: ', res)

def opcion2():
    print('Cantidad de silabas diferentes...')
    n = validar_mayor_que(0)
    tp = permutaciones_sin_reposicion(n,n)
    print('Permutaciones de ', n, ' silabas tomadas de a', n , ":", tp)

def opcion3():
    print('Cantidad de agentes...')
    n = validar_mayor_que(0)
    print('Cantidad de agenetes por grupo...')
    m = validar_intervalo(0,n)
    tp = combinaciones_sin_reposicion(n,m)
    print('Combinaciones de ', n, ' agentes tomados en grupos de a', m , ":", tp)
def opcion4():
    print('Cantidad de pilotos...')
    n = validar_mayor_que(0)
    print('Cantidad de puestos con puntaje...')
    m = validar_mayor_que(0)
    tp = permutaciones_sin_reposicion(n,m)
    print('Combinaciones de ', n, ' pilotos tomados de a', m , ":", tp)
def opcion5():
    n = 27
    print('La cantidad de letras a combinar son ', n)
    print('Cantidad de posiciones en cada clave...')
    k = validar_mayor_que(0)
    tp = permutaciones_con_reposicion(n,k)
    print('permutaciones de ', n, ' letras tomadas de a', k  , "con repeticiones:", tp)
def opcion6():
    print('cantidad de colores...')
    n = validar_mayor_que(0)
    print('cantidad de fichas a extraer...')
    m = validar_mayor_que(0)
    tp = combinaciones_con_reposicion(n,m)
    print('Combinaciones de', n,'colores tomados de a', m, 'con reposicion:', tp)

def menu():
    print('Menu de opciones - Calculo combinatorio')
    op = 1
    while op != 7:
        print('\n')
        print(' 1 - Total de ofertas de vehiculos ')
        print(' 2 - permutaciones de silabas ')
        print(' 3 - combinacion de agentes de seguridad ')
        print(' 4 - Permutaciones de pilotos de carreras ')
        print(' 5 - Permutaciones de letras en una clave')
        print(' 6 - Combinaciones de colores ')
        print(' 7 - Salir ')
        op  = int(input('Ingree el numero de la opcion elegida: '))
        
        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
        elif op == 4:
            opcion4()
        elif op == 5:
            opcion5()
        elif op == 6:
            opcion6()
menu()