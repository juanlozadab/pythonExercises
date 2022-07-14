from email.headerregistry import DateHeader


first_num = 6
second_num = 2
print(first_num - second_num)
print(first_num ** second_num)
# + -> addition
# - -> substraction
# * -> multiplication
# / -> division
# ** -> exponent
days_in_feb = 28
# intenta sumar un int y un str por lo que tira error
# print(days_in_feb + ' days in feb')
# hay que convertir 
print(str(days_in_feb) + ' days in february')

# input siempre da un str
first = input('Ingresa el primer numero: ')
second = input('Ingresa el segundo numero: ')

print(first + second) #devuelve concatenacion
print(int(first) + int(second)) # devuelve suma
