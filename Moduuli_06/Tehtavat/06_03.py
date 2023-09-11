def gal_lit(x):
    lit = x * 3.785412
    return lit


gallons = 0
a = True
while a:
    gallons = float(input("Anna gallonamäärä: "))
    if gallons < 0:
        exit()
    liters = gal_lit(gallons)
    print(f"{gallons} gallonaa on {liters} litraa")
