# Cargar por teclado un conjunto de numeros enteros, uno a uno. la carga solo debe terminar cuando se ingrese el cero.
# determine si los numeros que se ingresaron eran todos positivos o negativos (sin importar en que orden hayan entrado)
# por ej, la secuencia {8,4,3,7 } cumple con la consigna indicada, la secuencia {-2,-2,-8} son todos negativos, pero si 
# hay positivos y negativos no aplica, muestre la suma de los numeros si aplica.
actual = int(input('Ingrese un numero: '))
suma = 0
ok = True
anterior = actual
while actual != 0:
    if actual * anterior < 0:
        ok = False
    suma += actual
    anterior = actual     
    actual = int(input('Ingrese otro numero: '))
if ok:
    print('Todos los numeros eran del mismo signo, la suma es: ', suma )
else:
    print('habia numeros de distintos simbolos')
