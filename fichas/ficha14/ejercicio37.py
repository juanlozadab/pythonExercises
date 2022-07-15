# Desarrollar un programa que permita cargar tres arreglos con n nombres de
# personas, sus edades y los sueldos que ganan. Luego de realizar la carga de todos los datos,
# mostrar los nombres de las personas mayores de 18 años que ganan menos de 10000 pesos,
# pero de forma que el listado salga ordenado en forma alfabética.

# cargar por teclado los tres arreglos
from wsgiref import validate


def read(nombres, edades, sueldos):
    n = len(nombres)
    for i in range(n):
        nombres[i] = input('Nombre [' + str(i) +']: ')
        edades[i] = int(input('Edad: '))
        sueldos[i] = int(input('Sueldo: '))
        print()
# ordenar los arreglos (seleccion directa)
def sort(nombres,edades,sueldos):
    n = len(nombres)
    for i in range(n -1):
        for j in range(i+1, n):
            if nombres[i] > nombres[j]:
                nombres[i] , nombres[j] = nombres[j] , nombres[i]
                edades[i] , edades[j] = edades[j] , edades[i]
                sueldos[i] , sueldos[j] = sueldos[j] , sueldos[i]
#mostrar datos
def display(nombres,edades,sueldos):
    n = len(nombres)
    print('Mayores de 18 que ganan menos de 10000 pesos: ')
    for i in range(n):
        if edades[i] > 18 and sueldos[i] < 10000:
            print('Nombre: ', nombres[i] , ' ;Edad: ', edades[i], ' ;Sueldo: ', sueldos[i])

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Cantidad de elementos (> a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n
def test():
    n = validate(0)
    nombres = n * [0]
    edades = n * [0]
    sueldos = n * [0]
    read(nombres,edades,sueldos)
    sort(nombres,edades,sueldos)
    display(nombres,edades,sueldos)
test()