import random
numcode3 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
numcode4 = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))

print(f"Kolminumeroinen lukukoodi, jonka luvut ovat väliltä 0 - 9:\n"
      f"{numcode3}")
print(f"Nelinumeroinen lukukoodi, jonka luvut ovat väliltä 1 - 6\n"
      f"{numcode4}")
