
def caracter_unico(cadena):
    n = len(cadena)
    if n == 0:
        return False
    c0 = cadena[0]
    for i in range(1,n):
        if c0 != cadena[i]:
            return False
    return True