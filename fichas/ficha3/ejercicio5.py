# La fuerza de atraccion entre dos masas m1 y m2 separadas por una distancia d esta 
# dada por la siguiente formula de la mecanica clasica:
# F = G * ((m1 * m2) / d^2)
# con G = 6.673x10^-8 (cte de gravitacion universal)
# Escribir un programa que cargue las masas m1 y m2 de dos cuerpos y la distancia d entre ellos 
# y muestre el valor de la intensidad de la fuerza de atraccion entre esos cuerpos

m1 = float(input('Masa 1: '))
m2 = float(input('Masa 2: '))
d = float(input('Distancia entre las masas: '))

G = 6.673 * pow(10,-8)
F =  G * ((m1 * m2) / d**2 )

print('la fuerza de atraccion entre las masas es de: ', F)