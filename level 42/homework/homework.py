
def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

def find_next_square(sq):
    if (sq ** 0.5).is_integer():
        return int((sq ** 0.5 + 1) ** 2)
    else:
        return -1

def row_sum_odd_numbers(n):
    first_number = n * (n - 1) + 1
    row_sum = sum(first_number + 2 * i for i in range(n))
    return row_sum

