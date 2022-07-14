# Se tienen los datos de tres postulantes a un empleo. a los que se les realizo un test para conocer el nivel de 
# formacion previa de cada uno, por cada postulante, se tienen entonces los siguientes datos: nombre del postulante,
# cantidad total de preguntas que le realizaron y cantidad de preguntas que contesto correctamente.
# Se pide confeccionar un programa que lea los datos de los tres postulantes, informe el nivel de formacion previa de 
# cada uno segun los criterios de aprobacion que se indican mas abajo, e indique finalmente el nombre del postulante que
# gano el puesto. los criterios de aprobacion son los siguientes, en funcion del porcentaje de rtas sobre el total
# de preguntas realizadas a cada postulante:
# Nivel superior - Porcentaje >= 90%
# Nivel medio - 75% <= Porcentaje < 90%
# Nivel regular - 50% <= Porcentaje < 75%
# Fuera de nivel - Porcentaje < 50%

def test():
    print('Seleccion de nuevo personal para una empresa..')
    for i in range(1,4):
        nom = input('Ingrese el nombre del postulante: ')
        tp = int(input('Total de preguntas: '))
        cpbr = int(input('Cantidad de preguntas bien respondidas: '))

        pr = porcentaje(tp, cpbr)

        print('Nombre', i , ':',nom, ' - Nivel: ', nivel(pr), ' - porcentaje: ', pr, '%')

def porcentaje(tp , pbc):
    return pbc * 100 / tp
def nivel(pr):
    if pr >= 90:
        return 'Superior'
    elif pr >= 75:
        return 'Medio'
    elif pr >= 50:
        return 'Regular'
    else:
        return 'Fuera de Nivel'

test()