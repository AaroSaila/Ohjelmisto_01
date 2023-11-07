while True:
    isPrime = True
    num = int(input("Anna kokonaisluku: "))
    x = range(2, num)
    if num <= 1:
        isPrime = False
    else:
        for t in x:
            if num % t == 0:
                isPrime = False

    if isPrime:
        print(f"Luku {num} on alkuluku.")
    else:
        print(f"Luku {num} ei ole alkuluku.")
