# Se cargan por teclado dos numeros, calcular la superficie de un cuadrado, suponiendo como lado del mismo al mayor
# de los numeros dados y la superficie de un circulo suponiendo como radio del mismo al menor de los numeros dados

from cmath import pi


n1 = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese un numero: '))

if n1 < n2:
    menor = n1
    mayor = n2
else:
    menor = n2
    mayor = n1
sup_cuad = mayor**2
sup_circ = 2*pi*menor

print('la superficie del cuadrado es: ', sup_cuad)
print('la superficie del circulo es: ', sup_circ)
