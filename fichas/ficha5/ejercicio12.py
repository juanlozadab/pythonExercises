# Una compañia de alquiler de automoviles necesita un programa que calcule lo que se debe cobrar al cliente,
# teniendo en cuenta el kilometraje recorrido por el cliente al devolver el automovil
#  - Si el cliente no supero los 300 km recorridos se debera cobrar 500
#  - Para recorridos desde 300 a 1000 km se le cobrara 500 mas el excedente a razon de 3$ x km
#  - Para recorridos de mas de 1000 km se cobrara los 500 y 1.5$ x km 

km = int(input('Ingrese la cantidad de km recorridos: '))

if( km <= 300):
    monto = 500
elif( km > 300 and km <= 1000):
    monto = 500 + ((km-300)*3)
else:
    monto = 500 + ((km-300)*1.5)

print('se le debe cobrar: ', monto)