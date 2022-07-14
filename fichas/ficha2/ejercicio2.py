# Se conoce la cantidad de horas que trabaja un empleado en una fabrica, 
# mas el importe que recibe por cada hora de trabajo, ademas del nombre del empleado.
# se pide calcular y mostrar el nombre del empleado y el importe final del sueldo que el empleado debera cobrar.

# resultado -> nombre del empleado (nom: str) ; sueldo final (sueldo: float)
# datos -> nombre (nom: str) ; horas trabajadas ( horas: int) ; monto x hora (monto: float)
# proceso -> sueldo = horas * monto

nombre = input('Ingrese el nombre del empleado: ')
horas = int(input(f'Ingrese la cantidad de horas que trabajo {nombre}: '))
monto = float(input(f'Ingrese el monto por hora que le corresponde a {nombre}: '))

sueldo = horas * monto

print(f'el sueldo de {nombre} es {sueldo}')
