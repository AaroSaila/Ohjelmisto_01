year = int(input("Anna vuosiluku: "))

if (year % 4) == 0 and (year % 100) != 0:
    print(f"Vuosi {year} on karkausvuosi.")
elif (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0:
    print(f"Vuosi {year} on karkausvuosi.")
else:
    print(f"Vuosi {year} ei ole karkausvuosi.")