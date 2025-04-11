def how_many_light_sabers_do_you_own(name=""):
    return 18 if name == "Zach" else 0
    
def stringy(size):
    return ''.join('1' if i % 2 == 0 else '0' for i in range(size))

def get_grade(s1, s2, s3):
    avarage = (s1 + s2 + s3) / 3
    if avarage >= 90:
        return 'A'
    elif avarage >= 80:
        return 'B'
    elif avarage >= 70:
        return 'C'
    elif avarage >= 60:
        return 'D'
    else:
        return 'F'
    
def fake_bin(x):
    return ''.join(['0' if int(digit) < 5 else '1' for digit in x])

def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump

def better_than_average(class_points, your_points):
    avarage = sum(class_points) / len(class_points)
    return your_points > avarage

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
def abbrev_name(name):
    parts = name.split()
    initials = parts[0][0].upper() + '.' + parts [1][0].upper()
    return initials

def lovefunc( flower1, flower2 ):
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)

def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    highest = max(num_list)
    lowest = min(num_list)
    return f"{highest} {lowest}"

def solution(text, ending):
    return text.endswith(ending)

def binary_array_to_number(arr):
    binary_string = ''.join(map(str, arr))
    return int(binary_string, 2)

def xo(s):
    s = s.lower()
    c_x = s.count('x')
    c_o = s.count('o')
    return c_x == c_o

def solution(nums):
    if nums is None or len(nums) == 0:
        return []
    return sorted(nums)