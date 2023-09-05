from random import randint

dice = int(input("Anna noppien lukumäärä: "))

for n in range(dice):
    print(randint(1, 6))
