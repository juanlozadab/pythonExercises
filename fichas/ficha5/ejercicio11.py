# Cargar por teclado tres numeros enteros y determinar y mostrar el mayor de ellos. 
# No utilice para el proceso la funcion max() de la libreria estandar de Python

n1 = int(input('Ingrese un numero:')) 
n2 = int(input('Ingrese un numero:'))
n3 = int(input('Ingrese un numero:'))

if( n1 > n2 and n1 > n3):
    mayor = n1
elif( n2 > n1 and n2 > n3):
    mayor = n2
else:
    mayor = n3
print('El mayor es: ', mayor)
