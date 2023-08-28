import random

numcode3 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
numcode4 = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))

print("Kolminumeroinen lukukoodi, jonka luvut ovat väliltä 0 - 9:\n" + numcode3)
print("\nNelinumeroinen lukukoodi, jonka luvut ovat väliltä 1 - 6:\n" + numcode4)
