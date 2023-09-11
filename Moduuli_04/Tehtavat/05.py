# käyttäjätunnus = python
# salasana = rules

tries = 0

while tries < 5:
    username = input("Anna käyttäjätunnus: ")
    password = input("Anna salasana: ")
    tries = tries + 1
    if username == "python" and password == "rules":
        print("Tervetuloa")
        break
else:
    print("Pääsy evätty.")