#1
n1=10
n2=25

n3 = n1 + n2
print(n3)

#2
str1="hello "
str2="world"
str3 = str1 + str2
print(str3)
#concatenation is joining two or more strings to create new sring

#3

n4=100
n5=5
n6 = n4 / n5
print(n6)
#it sh0ws always float so you can see more precise divison results always its implicit

#4

print(n2+n1)
print(n2-n1)
print(n2*n1)
print(n2/n1)
print(n2<n1)
print(n2>n1)

#5

print(30+50 <= 100+50)
print(30+50 >= 100+50)
print(30+50 == 100+50)

#6

print(10>5 and 5<11)
print(10<5 and 5<11)
print(10>5 and 5>11)
print(10<5 and 5>11)
print(100<5 or 100>90)
print(100>5 or 100>90)
print(100>5 or 100<90)
print(100<5 or 100<90)

#7

print(10>5 and 50<110)
print(10>20 or 200<110)
print(10>20 and 200<110)
print(14==50 and 50<11)
print(15>5 or 125==1)

#8

for i in range(1, 11):
    print(i)

#9

list1=[5, 10, 15, 20, 25]

sum=0

for num in list1:
    sum += num

print(sum)

#10

#?

#11

num1=1

while num1 <= 10:
    print(num1)
    num1+=1

#12

num2=1

while num2 <= 100:
    if 50 <= num2 <= 60:
        num2 += 1
        continue
    else:
        print(num2)
    num2 += 1

#13

#?

#14

def if_divs_3_5(number):
    return number % 3 == 0 and number % 5 == 0

input = int(input("Enter a number: "))
if if_divs_3_5(input):
    print(f"{input}is divisible by both 3 and 5.")
else:
    print(f"{input} is not divisible by both 3 and 5.")

#15

#?

#16

#?

#17

#?

