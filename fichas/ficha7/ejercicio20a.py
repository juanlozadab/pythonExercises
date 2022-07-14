# El juego del numero secreto consiste en lo siguiente: la computadora tiene un numero guardado (que el
# jugador no conoce) y el jugador debe tratar de adivinarlo. si lo logra gana el juego y la computadora le 
# avisa en cuantos intentos lo realizo. si no lo logra en una cierta cantidad de intentos predefinida, el juego
# termina y se avisa que el jugador ha perdido. la cantidad maxima de intentos es un valor que debe cargarse por teclado
# al igual que el limite derecho del intervalo que contendra al numero secreto elegido

import random


fin_intervalo = int(input('Ingrese el numero del fin del intervalo: '))
intentos = int(input('Ingrese la cantidad maxima de intentos: '))
num_int = 0
encontro = False
numero_oculto = random.randint(1,fin_intervalo)
print(numero_oculto)

while num_int != intentos:
    num = int(input('Ingrese su numero: '))
    num_int += 1
    if num == numero_oculto:
        encontro = True
        break
    else:
        print('ufff estuviste cerca, continua asi!')
  
if(encontro == True):
    print('FELICITACIONES! ENCONTRASTE EL NUMERO OCULTO EN: ', num_int , ' intentos!')
else: 
    print('que lastima te has quedado sin mas intentos')