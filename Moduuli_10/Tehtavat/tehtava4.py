from random import randint


class Auto:
    def __init__(self, rekisterikilpi, huippunopeus):
        self.rekisterikilpi = rekisterikilpi
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
        self.sija = 0

    def properties(self):
        print(f"Auton ominaisuudet \n"
              f"rekisteritunnus: {self.rekisterikilpi} \n"
              f"huippunopeus: {self.huippunopeus} km/h \n"
              f"tämänhetkinen nopeus: {self.nopeus} km/h \n"
              f"kuljettu matka: {self.kuljettu_matka} km")

    def kulje(self, aika_h):
        self.kuljettu_matka += aika_h * self.nopeus


class Kilpailu:
    def __init__(self, nimi, pituus_km, autolista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.nopeus += randint(-10, 15)
            Auto.kulje(auto, 1)

    def tulosta_tilanne(self):
        sija = 1
        while sija < len(self.autolista) - 1:
            for auto in self.autolista:
                if auto.sija == sija:
                    print(f"""
------------------------------------------------------------------------------------------------------------------------   
{auto.rekisterikilpi} | Sija: {auto.sija} | Huippunopeus: {auto.huippunopeus} | Tämänhetkinen nopeus: {auto.nopeus} | Kuljettu matka: {auto.kuljettu_matka}
------------------------------------------------------------------------------------------------------------------------
                """)
            sija += 1
        return

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettu_matka >= self.pituus_km:
                auto.kuljettu_matka = self.pituus_km
                return True
            else:
                return False

    def katso_sija(self):
        cars = []
        for car in self.autolista:
            distance_to_goal = self.pituus_km - car.kuljettu_matka
            cars.append((distance_to_goal, car.rekisterikilpi))
        cars.sort()
        cars_dict = dict()
        for (k, v) in cars:
            cars_dict.update({v: cars.index((k, v))})
        for car in self.autolista:
            car.sija = cars_dict[car.rekisterikilpi] + 1


def create_cars(car_list, num):
    for i in range(1, num+1):
        car_list.append(Auto("ABC-" + str(i), randint(100, 200)))
    return


def race(race_name):
    tunti = 0
    while not Kilpailu.kilpailu_ohi(race_name):
        for i in range(10):
            Kilpailu.tunti_kuluu(race_name)
            Kilpailu.kilpailu_ohi(race_name)
        tunti += 10
        print(f"Tunti {tunti}")
        Kilpailu.katso_sija(race_name)
        Kilpailu.tulosta_tilanne(race_name)
    print("Kilpailu on päättynyt.")
    Kilpailu.katso_sija(race_name)
    Kilpailu.tulosta_tilanne(race_name)


def main():
    cars = []
    create_cars(cars, 10)
    suuri_romuralli = Kilpailu("Suuri romuralli", 8000, cars)
    race(suuri_romuralli)


main()
