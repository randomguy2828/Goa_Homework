def human_years_cat_years_dog_years(human_years):
    cat_years = 15 if human_years >= 1 else 0
    dog_years = 15 if human_years >= 1 else 0
    if human_years >= 2:
        cat_years += 9
        dog_years += 9
    if human_years >= 3:
        cat_years += 4 * (human_years - 2)
        dog_years += 5 * (human_years - 2)
    return [human_years, cat_years, dog_years]

def first_non_consecutive(arr):
    if not arr or len(arr) == 1:
        return None
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
        
def to_alternating_case(string):
    result = []
    for char in string:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')

def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"
