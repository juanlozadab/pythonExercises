# Desarrollar un programa controlado por menu de opciones, que incluya opciones para realizar las siguientes tareas
# 1 - cargar un valor entero n por teclado, y obtener la suma de los enteros del 1 al n
# 2 - cargar un valor entero n por teclado y obtener su factorial
# 3 - cargar por teclado los coeficientes a, b, c de un polinomio de gugundo grado y obtener el valor del polinomio
#     en el punto c siendo x un valor que tambien se carga por teclado

op = 1

while op != 4:
    #vemos las opciones
    print('----------------------------------------------')
    print('1 - Suma de 1 al n ')
    print('2 - Factorial de n ')
    print('3 - Polinomio valuado en x')
    print('4 - Salir')
    print('----------------------------------------------')
    
    op = int(input('Ingrese la opcion elegida: '))
    print('\n')
    if op == 1:
        n = -1
        while n < 0:
            n = int(input('Ingrese el valor de n: '))
            if n < 0: 
                print('\nERROR--- n no puede ser negativo')
        suma = 0
        for i in range(n+1):
            suma += i
        
        print('\nla suma de 1 a n es: ', suma , '\n')
    elif op == 2:
        n = -1
        while n < 0:
            n = int(input('Ingrese el valor de n: '))
            if n < 0: 
                print('ERROR--- n no puede ser negativo')
        fact = 1
        for i in range(2, n+1):
            fact *= i
            
        print('El factorial de n es: ', fact)    
    elif op == 3:
        a = int(input('Ingrese el valor de a: '))
        b = int(input('Ingrese el valor de b: '))
        c = int(input('Ingrese el valor de c: '))
        x = int(input('Ingrese el valor de x: '))
        y = a*(x**2) + b*x + c
        print('el valor del polinomio en x es: ', y)
    elif op == 4:
        break 