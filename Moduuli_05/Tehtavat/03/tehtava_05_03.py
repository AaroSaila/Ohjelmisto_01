while True:
    a = []
    num = int(input("Anna kokonaisluku: "))
    x = range(1, num+1)
    for t in x:
        y = num % t
        a.append(y)
    if a.count(0) == 2:
        print(f"Luku {num} on alkuluku.")
    else:
        print(f"Luku {num} ei ole alkuluku.")
