def greet(name):
    return f"Hello, {name} how are you doing today?"

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

def check_alive(health):
    return health > 0

def well(x):
    count_good = x.count("good")
    if count_good == 0:
        return "Fail!"
    elif count_good <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
    
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

def bin_to_decimal(inp):
    return int(inp, 2)

def position(letter):
    return f"Position of alphabet: {ord(letter) - ord('a') + 1}"

def generate_range(start, stop, step):
    return list(range(start, stop + 1, step))

def define_suit(card):
    suits = {"C": "clubs", "D": "diamonds", "H": "hearts", "S": "spades"}
    return suits[card[-1]]

def multiply(n):
    num_digits = len(str(abs(n))) 
    return n * (5 ** num_digits)

def break_chocolate(n, m):
    if n <= 0 or m <= 0:
        return 0  
    return n * m - 1

def max_multiple(divisor, bound):
    return (bound // divisor) * divisor

def even_numbers(arr, n):
    evens = [num for num in arr if num % 2 == 0]
    return evens[-n:]