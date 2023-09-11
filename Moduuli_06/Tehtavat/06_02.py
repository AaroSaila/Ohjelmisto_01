from random import randint


def dice(x):
    num = randint(1, x)
    return num


a = 0
sides = int(input("Anna nopan sivujen määrä: "))

i = 0
while a != sides:
    a = dice(sides)
    i += 1
    print(a)

print(f"Heittokertoja oli {i}")
