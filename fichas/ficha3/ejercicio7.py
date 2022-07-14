# Una pequeña oficina de correos dispone de cinco casillas o boxes para guardar las
# cartas que debe despachar. Cada casilla (que puede contener muchas cartas) está numerada con
# números correlativos del 0 al 4. Cada carta que se recibe tiene un código postal numérico, y en base a
# ese código el despachante debe determinar en qué box guardará la carta, pero de tal forma que el
# mismo sistema sirva luego para saber en qué caja buscar una carta, dado su código postal. Diseñe un
# esquema de distribución que permita cumplir este requerimiento, cargando por teclado el código
# postal de tres cartas y mostrando en qué casilla será almacenada cada una.

n = 5

c1 = int(input('Ingrese el primer codigo postal: '))
c2 = int(input('Ingrese el segundo codigo postal: '))
c3 = int(input('Ingrese el tercero codigo postal: '))

n1 = c1 % n
n2 = c2 % n
n3 = c3 % n

print('codigo postal: ' , c1 , '\tasignado al box: ', n1)
print('codigo postal: ' , c2 , '\tasignado al box: ', n2)
print('codigo postal: ' , c3 , '\tasignado al box: ', n3)