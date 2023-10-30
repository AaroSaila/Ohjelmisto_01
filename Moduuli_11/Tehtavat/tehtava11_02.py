from random import randint


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus  # km/h
        self.nopeus = 0  # km/h
        self.ajettu_matka = 0 # km

    def aja(self, tuntimaara):
        self.ajettu_matka += self.nopeus * tuntimaara


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti  # kW/h


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko  # l


def main():
    polttoauto1 = Polttomoottoriauto("ACD-123", 165, 32.3)
    sahkoauto1 = Sahkoauto("ABC-15", 180, 52.5)

    polttoauto1.nopeus = randint(10, polttoauto1.huippunopeus)
    sahkoauto1.nopeus = randint(10, sahkoauto1.huippunopeus)

    polttoauto1.aja(3)
    sahkoauto1.aja(3)

    print(f"Polttomoottoriauton matkamittarilukema: {polttoauto1.ajettu_matka}\n"
          f"Sähköauton matkamittarilukema: {sahkoauto1.ajettu_matka}")


main()
