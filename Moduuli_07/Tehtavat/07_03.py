airports = dict()
escape = "tai syötä tyhjä merkkirivi palataksesi alkuun"


def new_airport(dicti):
    icao = input("Anna lentoaseman ICAO-koodi: ")
    name = input(f"Anna lentoaseman nimi {escape}: ")
    if name == "":
        return
    dicti[icao] = name
    print(airports)


def search_new_airport(icao, dicti):
    name = input(f"Anna lentoaseman {icao} nimi {escape}: ")
    if name == "":
        return
    dicti[icao] = name
    print(airports)


def search(dicti):
    icao = input(f"Anna haettavan lentoaseman ICAO-koodi {escape}: ")
    if icao == "":
        return
    while icao not in dicti:
        choice1 = input("Antamaasi lentoasemaa ei löytynyt. Haluatko lisätä lentoaseman? (Y/N): ").lower()
        while choice1 != "y" and choice1 != "n":
            choice1 = input("Haluatko lisätä lentoaseman? (Y/N): ")
        if choice1 == "y":
            search_new_airport(icao, airports)
            return
        else:
            icao = input(f"Anna haettavan lentoaseman ICAO-koodi {escape}: ")
            if icao == "":
                return
    name = dicti[icao]
    print(f"Lentokentän {icao} nimi on {name}.")
    return


while True:
    choice = input("\nHaluatko: \n 1. Lisätä lentoasematietoja \n 2. Hakea lentoasematietoja \n"
                   " 3. Lopettaa ohjelman suorittamisen \nVastaus: ")

    if choice == "1":
        print("")
        new_airport(airports)

    elif choice == "2":
        print("")
        search(airports)

    elif choice == "3":
        exit()
