from random import randint


def karsija(lista):
    b = []
    for t in lista:
        if t % 2 != 0:
            b.append(t)
    for t in b:
        lista.remove(t)
    return lista


a = []
for i in range(0, 10):
    a.append(randint(0, 100))
print(a)
print(karsija(a))
