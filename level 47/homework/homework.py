def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def grow(arr):
    result = 1  
    for num in arr:
        result *= num  
    return result

def check(seq, elem):
    return elem in seq

def reverse_seq(n):
    return list(range(n, 0, -1))

def sum_mix(arr):
    return sum(int(x) for x in arr)

def switch_it_up(number):
    words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return words[number]

def plural(n):
    return n != 1

def get_char(c):
    return chr(c)

def problem(a):
    if isinstance(a, str): 
        return "Error"
    return a * 50 + 6  

def capitalize_word(word: str) -> str:
    return word[0].upper() + word[1:]