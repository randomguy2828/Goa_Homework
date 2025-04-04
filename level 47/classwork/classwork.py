def solution(string):
    return string[::-1]

def positive_sum(arr):
    return sum(a for a in arr if a > 0)

def remove_char(s):
    return s[1:-1]

def square_sum(numbers):
    return sum(x**2 for x in numbers)

def find_smallest_int(arr):
    return min(arr)

def count_sheeps(sheep):
    return sum(1 for s in sheep if s)

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    
def litres(time):
    return int(time * 0.5)

def sum_array(a):
    total = 0
    for num in a:
        total += num 
    return total

def make_upper_case(s):
    return s.upper()

def smash(words):
    return ' '.join(words)

def hero(bullets, dragons):
    return bullets >= dragons * 2

def dna_to_rna(dna):
    return ''.join( ['U' if base == 'T' else base for base in dna])

def minimum(arr):
    return min(arr) if arr else None

def maximum(arr):
    return max(arr) if arr else None
    
