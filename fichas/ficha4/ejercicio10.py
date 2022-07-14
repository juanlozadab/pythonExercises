# Cargar por teclado tres numeros enteros que se supone que representan las edades de tres personas.
# determinar si alguno de los valores cargados era negativo, en cuyo caso informe en pantalla con un 
# mensaje tal como: alguna es incorrecta: negativa. si todos los valores eran positivos o cero informe 
# que todas eran correctas

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))

if( n1 < 0 or n2 < 0 or n3 < 0):
    print('Alguna es incorrecta: negativa.')
else:
    print('Todas eran correctas')