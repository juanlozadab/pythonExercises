# Un pequeño comercio de papelería cuenta con dos vendedores. Cada vendedor está
# codificado con los números 1 y 2. Considere que la carga de datos se realizará desde teclado, de
# forma que una entrada consta de 3 variables que representan una venta realizada: por cada venta,
# cargar el código del vendedor (1 o 2) que hizo la venta, cantidad de artículos vendida en esa
# operación, e importe de la venta. El fin de datos se indicará con código de vendedor igual a 0 (cero).
# El dueño del comercio desea cierta información estadística y para ello solicita un programa que
# obtenga lo siguiente:
# a.) La cantidad de productos vendida por cada vendedor (dos totales).
# b.) El importe total vendido por cada vendedor (otros dos totales).
# c.) El importe de la menor venta realizada por el vendedor 2.
# d.) El importe promedio de ventas por vendedor (importe total acumulado / 2).

# pasó la primera venta del vendedor 2?
aviso = False
# si no se cargan ventas del vendedor 2, menor_importe queda en None...
menor_importe = None
# acumuladores de cantidades...
c1 = c2 = 0
# acumuladores de importes...
i1 = i2 = 0
print('Ventas de un Comercio... ingrese los datos de cada venta...')
# ingresar (y validar) el primer codigo...
codigo = -1
while codigo != 0: 
    codigo = int(input('Ingrese el codigo del vendedor:'))

    if(codigo == 1 or codigo == 2):
        cantidad = int(input('Ingrese la cantidad: '))
        importe = float(input('Ingrese el importe: '))
        if codigo == 1:
            c1 += cantidad
            i1 += importe 
        elif(codigo == 2):
            c2 += cantidad
            i2 += importe
            if(not aviso):
                menor_importe = i2
                aviso = True
            elif(menor_importe > i2):
                menor_importe = i2
            
    elif(codigo == 0):
        break
    else:
        print('codigo no valido.')
promedio = (i1 + i2 )/2

print('Cantidad de productos vendida por el vendedor 1:', c1)
print('Cantidad de productos vendida por el vendedor 2:', c2)
print('Importe total facturado por el vendedor 1:', i1)
print('Importe total facturado por el vendedor 2:', i2)
print('Importe de la menor venta del vendedor 2:', menor_importe)
print('Importe promedio entre los dos vendedores:', promedio)