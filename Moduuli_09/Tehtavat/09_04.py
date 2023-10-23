from random import randint


class Car:
    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        self.speed = 0
        self.traveled_distance = 0

    def properties(self):
        print(
            f"""
            Auton ominaisuudet
            +---------------------------------------------+
             rekisteritunnus: {self.plate}
            +---------------------------------------------+
             huippunopeus:    {self.top_speed:} km/h
            +---------------------------------------------+
             tämänhetkinen nopeus: {self.speed} km/h 
            +---------------------------------------------+
             kuljettu matka: {self.traveled_distance} km
            +---------------------------------------------+
            
            """)

    def change_speed(self, speed_change):
        if self.speed + speed_change > self.top_speed:
            self.speed = self.top_speed
        elif self.speed + speed_change < 0:
            self.speed = 0
        else:
            self.speed += speed_change

    def travel(self, time):
        self.traveled_distance += self.speed * time


cars = []
for i in range(1, 11):
    cars.append(Car("ABC-"+str(i), randint(100, 200)))

race = True

while race:
    for i in range(10):
        cars[i].change_speed(randint(-10, 15))
    for i in range(10):
        cars[i].travel(1)
    for i in range(10):
        if cars[i].traveled_distance >= 10000:
            race = False

for i in range(10):
    cars[i].properties()
