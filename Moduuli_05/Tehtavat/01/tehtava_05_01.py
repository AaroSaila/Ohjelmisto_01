from random import randint

summa = 0
dice = int(input("Anna noppien lukumäärä: "))
# a = []

for x in range(dice):
    silmaluku = randint(1, 6)
    # .append(silmaluku)
    summa += silmaluku

# print(a)
print(summa)