from random import randint


def dice():
    num = randint(1, 6)
    return num


a = 0

while a != 6:
    a = dice()
    print(a)
