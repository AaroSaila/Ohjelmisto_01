gender = input("Oletko mies vai nainen? ")
gender = gender.lower()
hemoglobin = float(input("Anna hemoglobiiniarvosi: "))

if gender == "mies":
    if hemoglobin < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobin > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

if gender == "nainen":
    if hemoglobin < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobin > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
