# Se conoce la cantidad total de personas que padecen cierta enfermedad en todo el pais, y tambien se sabe cuantas
# de esas personas viven en una ciudad determinada. se desea saber que porcentaje representan estas ultimas 
# sobre el total de enfermos del pais.

cantidad_enfermos_nacional = int(input('Cantidad de enfermos en el pais: '))
cantidad_enfermos_ciudad= int(input('Cantidad de enfermos en la ciudad: '))
# cen - 100%
# cec - X
# X = cec * 100 / cen
porcentaje = cantidad_enfermos_ciudad * 100 / cantidad_enfermos_nacional
print('el procentaje es: ', porcentaje, '%')