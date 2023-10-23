class Car:
    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        self.speed = 0
        self.traveled_distance = 0

    def properties(self):
        print(f"Auton ominaisuudet \n"
              f"rekisteritunnus: {self.plate} \n"
              f"huippunopeus: {self.top_speed} km/h \n"
              f"tämänhetkinen nopeus: {self.speed} km/h \n"
              f"kuljettu matka: {self.traveled_distance} km")

    def show_speed(self):
        print(f"Auton {self.plate} nopeus: {self.speed} km/h")

    def change_speed(self, speed_change):
        if self.speed + speed_change > self.top_speed:
            self.speed = self.top_speed
        elif self.speed + speed_change < 0:
            self.speed = 0
        else:
            self.speed += speed_change


car1 = Car("ABC-123", 142)

car1.properties()

car1.change_speed(30)
car1.change_speed(70)
car1.change_speed(50)

print("")
car1.show_speed()

car1.change_speed(-200)

print("")
car1.show_speed()
