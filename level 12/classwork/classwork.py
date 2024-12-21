age=int(input("write your age:"))
if (age >= 18):
    print("normal price")
elif (age <= 18):
    print("discount")


number=int(input("write your number of lottary:"))
if number == 6:
    print("you won a house")
elif number == 30:
    print("you won the tickets to hawai")
else:
    print("you won 1$")

age1=int(input("write your age:"))
student=(input("are you a student?"))
if (age <= 18):
    print("discount")
elif student == "yes":
    print("discount")
else:
    print("normal price")