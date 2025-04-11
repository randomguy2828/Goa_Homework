def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string_ if char not in vowels])

def odd_or_even(arr):
    total_sum = sum(arr)
    return "even" if total_sum % 2 == 0 else "odd"

def number(lines):
    return [f"{i+1}: {line}" for i, line in enumerate(lines)]

def sort_by_length(arr):
    return sorted(arr, key=len)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def angle(n):
    return (n - 2) * 180

def round_to_next5(n):
    return ((n + 4) // 5) * 5

def no_odds(values):
    return [x for x in values if x % 2 == 0]

def mxdiflg(a1, a2):
    if not a1 or not a2: 
        return -1
    max_a1 = max(len(x) for x in a1)  
    min_a1 = min(len(x) for x in a1)  
    max_a2 = max(len(x) for x in a2) 
    min_a2 = min(len(x) for x in a2)  
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1)) 

def sum_of_minimums(numbers):
    return sum(min(row) for row in numbers)
