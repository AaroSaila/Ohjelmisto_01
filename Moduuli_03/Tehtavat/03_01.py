zander = float(input("Anna kuhan pituus senttimetreinä: "))
minimum = 37

if zander <= minimum:
    print(f"Kuha on {(minimum - zander):.2f} cm alamittainen, heitä se takaisin järveen.")
else:
    print("Kuha ei ole alamittainen.")
