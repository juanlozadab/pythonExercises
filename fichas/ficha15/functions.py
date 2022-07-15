
def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese n (mayor a ' + str(inf) + 'por favor): '))
        if n <= inf:
            print('Error, se pidio mayor a ' ,inf)
    return n

def read_alt(alt):
    n = len(alt)
    print('Cargue ahora las alturas en cm del grupo...')
    for i in range(n):
        alt[i] = int(input('Altura['+ str(i) + ']: '))

def read(v):
    n = len(v)
    for i in range(n):
        v[i] = int(input('Valor['+ str(i) + ']: '))

def avarage(alt):
    n = len(alt)
    tot = 0
    for i in range(n):
        tot += alt[i]
    return tot / n

def count(alt, avg):
    n = len(alt)
    c1 = c2 = 0
    for i in range(n):
        if alt[i] > avg:
            c1 += 1
        else:
            c2 +=1
    return c1, c2

def generate(v1,v2):
    v3 = []
    n = len(v1)
    m = len(v2)
    for i in range(n):
        exists = False
        for k in range(len(v3)):
            if v3[k] == v1[i]:
                exists = True
                break
        if not exists:
            for j in range(m):
                if v1[i] == v2[j]:
                    v3.append(v1[i])
                    break
    return v3

def sequence(v ,k):
    n = len(v)
    for i in range(1, n):
        if v[i] != v[i-1] + k:
            return False
    return True