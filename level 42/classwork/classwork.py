def create_array(n):
    res=[]
    i=1
    while i<=n:
        res.append(i)
        i += 1
    return res

def get_real_floor(n):
    if n <= 0:
        return n
    elif n < 13:
        return n - 1
    else:
        return n - 2
    
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

def divisible_by(numbers, divisor):
    return list(filter(lambda num: num % divisor == 0, numbers))

def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])

def get_sum(a,b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

def friend(x):
    return [name for name in x if len(name) == 4]

def maskify(cc):
    return cc[-4:].rjust(len(cc), "#")

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))