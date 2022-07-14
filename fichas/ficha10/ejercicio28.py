# Una empresa de turismo que vende viajes para egresados de colegios secundariios ofrece a tres cursos 
# distintos la siguiente promocion: el costo del viaje por persona es de 1360, pero si el grupo excede 
# las cuarenta personas, la empresa realiza un descuento del 5% sobre el costo total del viaje para el 
# curso. Desarrollar un programa que cargando la cantidad de alumnos de cada uno de los tres cursos 
# permita determinar: 1 - el curso mas numeroso ; 2 - el monto del viaje de cada curso ; 
# 3 - el porcentaje que representa el monto del viaje del curso mas numeroso sobre el total de la ganancia

def test():
    print('SISTEMA DE COSTOS EMPRESA DE TURISMO')
    c1 = int(input('Ingrese la cantidad de alumnos del curso 1: '))
    c2 = int(input('Ingrese la cantidad de alumnos del curso 2: '))
    c3 = int(input('Ingrese la cantidad de alumnos del curso 3: '))

    may_cu, may  = mayor(c1,c2,c3)
    m1 , m2 , m3 = monto(c1,c2,c3)
    
    pr = porcentaje(may,m1,m2,m3)
    print('El curso mas numeroso es: ', may_cu , ' con: ', may, ' alumnos.')
    print('Los montos a pagar por cada curso son: ')
    print('Primer curso: ', m1)
    print('Segundo curso: ', m2)
    print('Tercer curso: ', m3)
    print('El porcentaje que representa el curso mas grande es: ', pr)
    

def mayor(c1,c2,c3):
    if c1 > c2 and c2 > c3:
        may = c1
        may_cu = 'Primero'
    elif c2 > c3:
        may = c2
        may_cu = 'Segundo'
    else:
        may = c3
        may_cu = 'Tercero'
    return  may_cu , may

def monto(c1,c2,c3):
    m1 = c1 * 1360
    m2 = c2 * 1360
    m3 = c3 * 1360
    if c1 > 40:
        m1 = m1 * 0.95
    if c2 > 40:
        m2 = m2 * 0.95 
    if c3 > 40:
        m3 = m3 * 0.95
    return m1, m2 ,m3
def porcentaje(may,m1,m2,m3):
    tot = m1 + m2 + m3
    mcg = may * 1360
    if may > 40:
        mcg = mcg * 0.95
    pr = mcg * 100 / tot
    return pr
test()