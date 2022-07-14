# En el contexto de un estudio estadistico, se requiere un programa que cargue tres numeros por teclado
# y luego proceda a determinar el menor de ellos y calcular el cuadrado y el cubo del mismo

n1 = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese un numero: '))
n3 = int(input('Ingrese un numero: '))

if( n1 < n2 and n1 < n3):
    menor = n1
elif( n2 < n3):
    menor = n2
else:
    menor = n3
cuad = menor**2
cubo = menor**3
print('El numero menor es: ', menor, ' el cuadrado de este es: ', cuad, ' y el cubo: ' , cubo)