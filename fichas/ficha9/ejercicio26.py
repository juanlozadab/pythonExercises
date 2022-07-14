# Dado un numero entero y positivo (que puede ser primo o no), determine el valor del primer numero primo que se mayor 
# a n.
def test():
    n = int(input('Ingrese el numero: '))
    prime = next_prime(n)
    print('El numero primo mas cerca de tu numero es: ', prime)
def next_prime(n):
    if n < 2:
        return 2
    p = n + 1
    if p % 2 == 0:
        p += 1
    while not is_prime(p):
        p += 2
    return p
def is_prime(n):
    if n < 0:
        return None
    if n == 1:
        return False
    if n == 2: 
        return True
    if n % 2 == 0:
        return False
    raiz = int(pow(n,0.5))
    for i in range(3,raiz+1, 2):
        if n % i == 0:
            return False
    return True
test()