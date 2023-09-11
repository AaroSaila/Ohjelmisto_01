from math import pi


def pricepsqrm(diameter, price):
    radius = diameter / 2
    area = pi * (radius ** 2)
    priceparea = price / area
    return priceparea


diameter1 = float(input("Anna pizzan 1 halkaisija: "))
price1 = float(input("Anna pizzan 1 hinta: "))
diameter2 = float(input("Anna pizzan 2 halkaisija: "))
price2 = float(input("Anna pizzan 2 hinta: "))

if pricepsqrm(diameter1, price1) < pricepsqrm(diameter2, price2):
    print("Pizza 1 on halvempi per neliömetri.")
else:
    print("Pizza 2 on halvempi per neliömetri.")
