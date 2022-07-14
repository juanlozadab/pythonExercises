# Determinar el mayor valor de una sucesión de valores que se cargan por teclado.
# Asuma en primera instancia que la cantidad n de números a procesar se conoce de antemano. Y
# luego de resolverlo con esa suposición, replantee su solución asumiendo que la cantidad n de
# números se desconoce y que la carga de datos terminará cuando se ingrese un 0.

# se conoce la cantidad

'''
cant = int(input('Ingrese la cantidad de numeros que se compararan: '))
if cant <= 0:
    print('no se ha hecho ninguna comparacion')
    exit()
num = int(input('Ingrese el primer valor:'))
for i in range(1,cant):
    if i == 1:
        mayor = num
    num = int(input('Ingrese un numero:'))
    if num > mayor:
        mayor = num
print('el mayor numero ingresado es: ', mayor)

'''
num = int(input('Ingrese un numero (con cero finaliza)'))
mayor = None
b = False

while num != 0:
    if b == False:
        mayor = num
        b = True
    if num > mayor:
        mayor = num
    num = int(input('Ingrese un numero (con cero finaliza)'))
print('el mayor es: ', mayor)