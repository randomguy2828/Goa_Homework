num1 = [i for i in range(1,101)]
print(num1)

num2 = [i for i in range(1, 101) if i % 2 == 0]
print(num2)

names = ["nika", "giorgi", "erekle", "dato"]
names = [i.capitalize() for i in names]
print(names)

num3 = [i ** 2 for i in range(1,10)]
print(num3)