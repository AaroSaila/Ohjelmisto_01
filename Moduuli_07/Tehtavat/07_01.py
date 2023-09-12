seasons = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
(winter, spring, summer, autumn) = seasons
seasons2 = ("talvi", "kevät", "kesä", "syksy")

month = int(input("Anna kuukauden järjestysluku: "))

for i in range(4):
    if month in seasons[i]:
        print(seasons2[i])
