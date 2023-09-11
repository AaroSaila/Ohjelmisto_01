from random import randint


def list_sum(x):
    result = sum(x)
    return result


a = []

for i in range(0, 10):
    a.append(randint(1, 1000))

print(a)
print(list_sum(a))
