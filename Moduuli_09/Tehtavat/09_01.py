class Auto:
    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        self.speed = 0
        self.traveled_distance = 0

    def properties(self):
        print(f"Auton ominaisuudet \n"
              f"rekisteritunnus: {self.plate: >13} \n"
              f"huippunopeus: {self.top_speed: >12} km/h \n"
              f"tämänhetkinen nopeus: {self.speed: >2} km/h \n"
              f"kuljettu matka: {self.traveled_distance: >8} km")
car1 = Auto("ABC-123", 142)

car1.properties()