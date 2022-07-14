# Dado el valor de los tres lados de un triangulo, calcular el perimetro del triangulo

# resultado -> el perimetro del triangulo (rtdo: float)
# datos -> los tres lados del triangulo (lad1,lad2,lad3: float)
# proceso -> p = lad1 + lad2 + lad3

print('Ejercicio 1 - Perimetro del triangulo')

lad1 = float(input('Ingrese el primer lado: '))
lad2 = float(input('Ingrese el segundo lado: '))
lad3 = float(input('Ingrese el tercer lado: '))

p = lad1 + lad2 + lad3

print('El perimetro es: ' , p)
