
def menor(n1,n2):
    if(n1 < n2):
        return n1
    return n2

def factorial(n):
    f = 1
    for i in range(2 , n+1 ):
        f *= i
    return f

def ordenar(n1,n2,ascendent = True):
    first, second = n2 , n1
    if n1 < n2:
        first , second = n1 , n2
    if not ascendent:
        first , second = second , first
    return first , second
    