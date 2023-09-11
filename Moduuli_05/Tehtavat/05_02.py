nums = []
num = input("Anna kokonaisluku: ")

while num != "":
    num = int(num)
    nums.append(num)
    num = input("Anna kokonaisluku, tai lopeta ohjelma enterillä: ")

for i in nums:
    if nums.count(i) > 1:
        nums.remove(i)

nums.sort(reverse=True)
print(f"Viisi suurinta antaamasi lukua olivat {nums[:5]}")
