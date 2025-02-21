def goals(laLiga, copaDelRey, championsLeague):
    total_goals = laLiga + copaDelRey + championsLeague
    return total_goals

def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result

def get_age(age):
    age_digit = int(age[0])
    return age_digit

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

def get_average(marks):
    total_sum = sum(marks)
    average = total_sum // len(marks)
    return average

def check_for_factor(base, factor):
    return base % factor == 0

def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    if n < 10:
        return "Keep at it until you get it"
    input(n)

