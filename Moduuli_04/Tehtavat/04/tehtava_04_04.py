import random

num = random.randint(1, 10)
guess = int(input("Tietokone on arvonnut luvun väliltä 1-10. Arvaa luku: "))

while guess != num:
    if guess > num:
        guess = int(input("Liian suuri arvaus. Arvaa uudelleen: "))
    if guess < num:
        guess = int(input("Liian pieni arvaus. Arvaa uudelleen: "))
else:
    print("Oikein")
