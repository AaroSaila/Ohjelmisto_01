import random

points = []
within = 0
calcs = 0
total = int(input("Kuinka monta pistettä lasketaan? "))
while True:

    while calcs < total:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        dot = str(x) + str(y)
        calcs = calcs + 1

        if (x ** 2) + (y ** 2) < 1 and dot not in points:
            within = within + 1
            points.append(dot)

    pi = 4 * within / total
    print(f"Piin likiarvo on {pi}.")