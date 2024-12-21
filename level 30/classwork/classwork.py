#NameError occurs when you try to use a variable or function name that has not been defined.
#SyntaxError means there's something wrong with the way the code is written.
#IndexError occurs when the index you chose is out of range.
#TypeError occurs when an operation or function is applied to an object of inappropriate type.
#ValueError occurs when a function receives an argument of the right type but inappropriate value.
my_variable=1
try:
    print(my_variable)
except: 
    print("'my_variable' is not defined.")

my_list = [1, 2, 3]

try:
    print(my_list[5])
except:
    print("That index is out of range.")

try:
    number = int("hello")
except:
    print("That's not a valid integer.")
