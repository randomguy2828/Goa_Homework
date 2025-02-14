def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]

def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]

a = "code"
b = "wa.rs"
name = a + b