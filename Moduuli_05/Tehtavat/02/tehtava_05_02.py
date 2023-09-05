nums = []
num = input("Anna kokonaisluku: ")

while num != "":
    num = int(num)
    nums.append(num)
    num = input("Anna kokonaisluku, tai lopeta ohjelma enterillä: ")

nums.sort(reverse=True)
print(f"Viisi suurinta antaamasi lukua olivat {nums[:5]}")
