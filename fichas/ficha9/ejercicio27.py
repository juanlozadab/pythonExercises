# dado un numero entero y positivo n, encontrar y mostrar su factorizacion.

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
    
def test():
    n = int(input('Ingrese el numero: '))
    print(factorizacion(n))
def factorizacion(n):
    # eliminamos casos no previstos
    if n < 0:
        print('se esperaba un numero positivo...')
        return
    # si n es primo, o es 1, mostrarlo y terminar 
    if n==1 or is_prime(n):
        print(n, end=' ')
        return
    # n no es primo
    # probar dividirlo por cada primo menor que n //2
    primo, producto = 2 , 1
    while primo <= n // 2:
        #si primo es divisor de n, mostrarlo pero tantas veces como la division sea posible
        cociente_parcial = n
        while cociente_parcial > 1 and cociente_parcial % primo == 0:
            print(primo, end=' ')
            producto *= primo
            cociente_parcial //= primo
            if producto == n:
                return
         #tomar el siguiente primo y seguir       
        primo = next_prime(primo)
test()
