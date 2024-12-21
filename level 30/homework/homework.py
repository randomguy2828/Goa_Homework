Name=1
try:
    print(Name)
except:
    print("there is no name")

list=["helooo"]
try:
    print(list[10])
except:
    print("That index is out of range.")

try:
    number = int(1,2,3,4,5)
except:
    print("That's not a valid integer.")

def summixedlist(numbers):
    return sum(int(num) for num in numbers)

print(summixedlist([10, "100", "19", 57,]))
