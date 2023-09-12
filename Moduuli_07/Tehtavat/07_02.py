a = set()
b = "0"
c = True

while c:
    b = input("Anna nimi: ")
    if b not in a and b != "":
        a.add(b)
        print("Uusi nimi")
    elif b == "":
        c = False
    else:
        print("Aiemmin syötetty nimi")

print("\nKaikki syötetyt nimet mielivaltaisessa järjestyksessä:\n")

for i in a:
    print(i)
