# Sea un numero entero mayor o igual a cero. el factorial del numero n (denotado algebraicamente como n!) es el producto
# de todos los numeros enteros en el intervalo [1,n] si n > 0. en caso de que n = 0 entonces 0! = 1.
# se pide desarrollar un programa de python que cargue por teclado un numero n y calcule y muestre su factorial.

num = int(input('Ingrese un numero: '))
if num == 0:
    print('el factorial es: 1')
elif num < 0:
    print('el numero ingresado no es valido')
else:
    rdo = 1 
    for i in range(num , 0 , -1):
        rdo *= i
       
    print('el factorial es: ',rdo)