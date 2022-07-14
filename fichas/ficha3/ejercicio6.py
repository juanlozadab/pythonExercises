# se necesita un programa que permita cargar el nombre de un estudiante de quinto, 
# el nombre del profesor responsable de su practica supervisada, y el promedio general 
# con decimales del estudiante. se pide simplemente mostrarlos en la consola de salida a modo de verificacion pero
# de forma que el nombre del estudiante este precedido de la cadena 'est.' y el nombre del profesor 'prof.'
# el promedio debera mostrarse redondeado en un numero entero

estudiante = input('Ingrese el nombre del estudiante: ')
promedio = float(input(f'Ingrese el promedio del estudiante {estudiante}:'))
profesor = input('Ingrese el nombre del profesor: ')
estudiante = 'est.' + estudiante
profesor = 'prof.' + profesor
print(estudiante)
print(profesor)
print('promedio: ' , int(round(promedio)))

