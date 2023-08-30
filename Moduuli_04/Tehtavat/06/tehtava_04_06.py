import random

within = 0
calcs = 0
total = int(input("Kuinka monta pistettä lasketaan? "))

while calcs < total:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    calcs = calcs + 1

    if (x ** 2) + (y ** 2) < 1:
        within = within + 1

pi = 4 * within / total
print(f"Piin likiarvo on {pi}.")
