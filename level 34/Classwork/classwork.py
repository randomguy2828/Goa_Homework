def manual_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = manual_map(square, numbers)
print(squared_numbers) 

square_numbers = list(map(lambda x: x ** 2, numbers))
print(square_numbers)

def manual_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

def greater_than_30(x):
    return x > 30

numbers1 = [-15, 45, 83, 57, 65, 70]
filt_num = manual_filter(greater_than_30, numbers1)
print(filt_num)

filt_num = list(filter(lambda x: x > 30, numbers1))
print(filt_num)