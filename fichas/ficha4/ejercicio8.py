# cargar por teclado dos nueros enteros, mostrarlos ordenados de menor a mayor

a = int(input('Ingrese el primer numero: '))
b = int(input('ingrese el segundo numero: '))

if(a > b):
    tupla = (b, a)
else:
    tupla = (a , b)
print(tupla)
