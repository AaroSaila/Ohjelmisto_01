inches = float(input("Anna tuumat: "))

while inches > 0:
    centimeters = inches * 2.54
    print(f"{inches:.2f} tuumaa on {centimeters:.2f} cm")
    inches = float(input("Anna tuumat: "))
