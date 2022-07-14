first_name = input('please enter your first name: \n')
last_name = input('please enter your last name: \n')
output = 'hello, ' + first_name + ' ' + last_name
output1 =  'hello, {} {} '.format(first_name, last_name)
output2 = 'hello, {0} {1}'.format(first_name, last_name)
#only in pyhon 3
output3 = f'hello, {first_name} {last_name}'
print(output)
print(output1)
print(output2)
print(output3)