# Se cargan tres numeros. se pide mostrarlos en pantalla ordenados de menor a mayor

a = int(input('Cargue un numero: '))
b = int(input('Cargue un numero: '))
c = int(input('Cargue un numero: '))

#comparo a y b para obtener mayor y menor
if(a < b):
    men = a
    may = b
else: 
    men = b
    may = a
#comparo el mayor con c y el menor con c
if( c > may):
    med = may
    may = c
elif(c < men):
    med = men
    men = c
else:
    med = c

#esta forma de resolver me permite mejorar la performance al no tener tantos condicionales

print(men, med, may)