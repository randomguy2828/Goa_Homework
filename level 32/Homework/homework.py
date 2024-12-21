numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

names = ["Alice", "Bob", "Charlie"]
greet = list(map(lambda name: "Hello," + name, names))
print(greet)

fruits = ["apple", "banana", "kiwi"]
length = list(map(len, fruits))
print(length)

numbers = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)

words = ["pear", "apple", "peach", "grape"]
words_starting = list(filter(lambda word: word.startswith("p"), words))
print(words_starting)  

numbers = [10, 55, 42, 78, 65, 20]
numbers_greater = list(filter(lambda x: x > 50, numbers))
print(numbers_greater)




