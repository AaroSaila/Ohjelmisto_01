import luokat

talot = []


def menu():
    print("""
1. Luo uusi talo
2. Aja hissiä
3. Palohälytys
4. Poistu
    """)
    choice = int(input(""))

    # Luo uusi talo
    if choice == 1:
        alin = int(input("Anna talon alin kerros: "))
        ylin = int(input("Anna talon ylin kerros: "))
        hissit_lkm = int(input("Anna talon hissien lukumäärä: "))
        talot.append(luokat.Talo(alin, ylin, hissit_lkm))
        print("Talo luotu")

    # Aja hissiä
    if choice == 2:
        for i in range(len(talot)):
            print(f"Talo {i+1}")
        talo = talot[int(input("Valitse talo ")) - 1]
        for i in range(len(talo.hissit)):
            print(f"Hissi {i+1}")
        hissi_nmro = int(input("Valitse hissi ")) - 1
        kerros = int(input(f"Valitse kerros ({talo.alin}-{talo.ylin}) "))
        luokat.Talo.aja_hissia(talo, hissi_nmro, kerros)

    if choice == 3:
        for talo in talot:
            luokat.Talo.palohalytys(talo)

    if choice == 4:
        exit()


while True:
    menu()
