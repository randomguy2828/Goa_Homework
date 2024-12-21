sum_numbers = lambda a, b: a + b

print(sum_numbers(100,500))

numbers_amplifie = lambda a: a * 2

print(numbers_amplifie(5))

range_list = lambda start, end: list(range(start, end))

print(range_list(1,100))

a = [5, 10, 15, 20]

triple = list(map(lambda x: x * 3, a))
print(triple)

a = [1, 2, 3, 4, 5,]

square = list(map(lambda x: x ** 2, a))
print(square)

celsius_temp = [0, 20, 30, 40]

cel_to_fah = lambda a: (a * 9/5) + 32

fahrenheit_temp = list(map(cel_to_fah, celsius_temp))

print(fahrenheit_temp)  

w = ["hello", "world", "python"]

capital_words = list(map(lambda word:word.capitalize(), w))

print(capital_words)

n = [1, 2, 3, 4, 5, 6, 7]

even_numbers = list(filter(lambda x:x % 2 == 0, n))

print(even_numbers)

word = ["cat", "house", "tree", "car"]

long_string = list(filter(lambda word: len(word) > 4, word))

print(long_string)

num = [3, 9, 15, 22, 27, 30]

div_by_three = list(filter(lambda x: x % 3 == 0, num))

print(div_by_three)
