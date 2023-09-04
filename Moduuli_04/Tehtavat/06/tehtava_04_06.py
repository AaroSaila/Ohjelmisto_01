from random import uniform

within = 0
calcs = 0
total = int(input("Kuinka monta pistettä lasketaan? "))

while calcs < total:
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    calcs += 1

    if (x ** 2) + (y ** 2) < 1:
        within += 1

pi = 4 * within / total
print(f"Piin likiarvo on {pi}.")
