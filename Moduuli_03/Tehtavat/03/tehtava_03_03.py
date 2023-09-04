gender = input("Oletko mies vai nainen? ").lower()
hemoglobin = float(input("Mikä on hemoglobiiniarvosi: "))

if gender != "mies" or gender != "nainen" or hemoglobin < 0:
    print("Virheelliset tiedot.")
    quit()

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
