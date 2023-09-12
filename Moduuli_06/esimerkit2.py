"""
Pääohjelman muuttujat = global-muuttujia
Aliohjelman muuttujat = local-muuttujia
"""


def print_city():
    # lokaali muuttuja, arvo käytössä vain funktion sisällä (local scope)
    city = "Helsinki"  # globaali muuttuja korvataan lokaalilla (funktion sisällä)
    city2 = "Vantaa"  # Turha muuttuja, siihen ei päästä pääohjelmasta käsiksi, eikä sillä tehdä funktiossa mitään.
    # return  # return voi toimia aliohjelmassa kuin silmukassa break
    print(city)


def print_city_v2():
    print(city2)


def print_city2():
    print(city)


def print_city3():
    city3 = "Hyvinkää"


def print_city4(city4):
    print(city4)


"----------------------------------------------------------------------------"

# globaali muuttuja, arvo käytössä koko ohjelman laajuisesti (global scope)
# (jossei sitä "ylikirjoiteta (shaodws)" funktion sisällä)
city = "Espoo"
print_city()  # printtaa print_city() sisäisen city-muuttujan
print(city)  # printtaa pääohjelman sisäisen city-muuttujan
# print(city2) # pääohjelma ei löydä muuttujaa määritellyn funktion sisältä

"-----------------------------------------------------------------------------"

# print_city_v2()  # Aliohjelmat eivät pääse käsiksi toisten aliohjelmien muuttujiin.

"-----------------------------------------------------------------------------"
print_city2()
# Jos muuttujaa ei ole määritelty aliohjelmassa, etsii se sen pääohjelmasta.

"-------------------------------------------------------------------------------"

# print(city3)
# Pääohjelmasta ei pääse käsiksi aliohjelmien muuttujiin.

"--------------------------------------------------------------------------------"

city4 = "Kirkkonummi"
print_city4(city4)
