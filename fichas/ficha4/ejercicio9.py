#cargar por teclado tres numeros enteros. determinar si el primero que se cargo es el mayor de los tres
n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))

if( n1 > n2 and n1 > n3):
    print('El Primero es el mayor')
else:
    print('El Primero no es el mayor')
