# Determinar si un numero entero n es primo o no. por ejemplo, el numero n = 28 no es primo ( ya que ademas de ser 
# divisible por 1 es divisible por 2 y por 7) pero n = 29 es primo ya que es divisible unicamente por 1 y por 29
def test():
    n = int(input('Ingrese el numero que quiere saber si es primo o no: '))
    prime = is_prime(n)
    if prime:
        print('El numero es primo')
    else:
        print('El numero no es primo')
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