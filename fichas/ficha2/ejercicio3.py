# Se tiene registrada la temperatura ambiente medida en tres momentos diferentes en un deposito de quimicos
# y se necesita calcular el valor promedio entre las temperaturas medidas, tanto en formato entero como en formato real

t1 = int(input('Ingrese la primer temperatura: '))
t2 = int(input('Ingrese la segunda temperatura: '))
t3 = int(input('Ingrese la tercera temperatura: '))

prom1 = (t1 + t2 + t3) / 3
prom2 = (t1 + t2 + t3) // 3

print('El promedio entero es: ' , prom2)
print('El promedio real es: ' , prom1)