num_large = ""
num_small = 0

while num_large == "":
    num1 = input("Anna luku: ")
    num_large = float(num1)
    num_small = float(num1)

while True:
    num1 = input("Anna luku: ")

    if num1 != "" and float(num1) > num_large:
        num_large = float(num1)
    if num1 != "" and float(num1) < num_small:
        num_small = float(num1)
    if num1 == "":
        break

print(f"\nSuurin syöttämäsi luku oli {num_large} ja pienin syöttämäsi luku oli {num_small}.")