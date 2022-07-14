# Desarrollar un programa en Python que permita cargar por teclado un texto
# completo (analizar dos opciones: una es cargar todo el texto en una variable de tipo cadena
# de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter uno por uno a
# través de un while). Siempre se supone que el usuario cargará un punto para indicar el final
# del texto, y que cada palabra de ese texto está separada de las demás por un espacio en
# blanco. El programa debe:
# a. Determinar cuántas palabras se cargaron.
# b. Determinar cuántas palabras comenzaron con la letra "p".
# c. Determinar cuántas palabras contuvieron una o más veces la expresión "ta".

from pickle import FALSE


cadena = input('Ingrese el texto que desea analizar: ')
palabras = 0
palabras_emp_p = 0
palabras_con_ta = 0
letra_t = False
nueva_palabra = True
primer_letra = True
for i in range(len(cadena)):
    letra = cadena[i]
    if letra == " " or letra == ".":
        #se termino una palabra
        palabras += 1
        primer_letra = True
        nueva_palabra = True
    else:
        if primer_letra == True:
            if(letra == 'p'):
                palabras_emp_p +=1
            primer_letra = False
        else:
            primer_letra = False
        
        if letra == 't' and nueva_palabra == True:
            letra_t = True
        elif letra == 'a' and letra_t == True and nueva_palabra == True:
            palabras_con_ta += 1
            nueva_palabra = False
        else:
            letra_t = False
print('Cantidad de palabras: ', palabras)
print('Cantidad de palabras que empiezan con p', palabras_emp_p)
print('Cantidad de palabras que tienen ta: ', palabras_con_ta)

            