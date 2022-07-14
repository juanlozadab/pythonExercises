# Desarrollar un programa que implemente el conocido juego de manos llamado 'piedra, papel y tijera'. en este juego
# participan dos jugadores,uno contra el otro. Cada uno fe ellos, al mismo tiempo que el otro debe mostrar con una de 
# sus manos, alguna de las tres figuras. luego se comparan las figuras que cada uno mostro y se determina quien gana.
import random


print ('---------------------------------------------')
print('Bienvenido al juego de piedra papel y tijera!')
print ('---------------------------------------------')
print('el juego es al mejor de tres. \n')

descripcion = 'Piedra','Papel','Tijera'
ganadasHum = ganadasCPU = 0
ganador = False
while not ganador:
    
    humano = int(input('Ingrese 1 - Piedra ; 2 - Papel ; 3 - Tijera: '))
    if(humano < 1 or humano > 3):
        print('La opcion ingresada no es valida , se asigna por defecto Piedra')
        humano = 1
    print('usted ha seleccionado: ', descripcion[humano-1])
    compu = random.randint(1,3)
    print('La computadora eligio: ', descripcion[compu-1])
    if( humano == compu ):
        print('Ambos eligieron lo mismo!')
    else: 
        if (humano == 1 and compu == 3) or (humano == 3 and compu == 2) or (humano == 2 and compu == 1):
            print('Ganaste esta mano!')
            ganadasHum +=1
        else:
            print('ohhh, perdiste esta mano!')
            ganadasCPU +=1
    if ganadasHum == 2:
        ganador = True
        print('Felicitaciones ganaste el juego')
    elif ganadasCPU == 2:
        ganador = True
        print('Tienes que practicar mas, has perdido ')
