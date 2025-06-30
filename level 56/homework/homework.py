def replace_g(word):
    parts = word.split("g")
    result = "G".join(parts)
    return result

def flip_case(word):
    flipped = ""
    for letter in word:
        if letter.islower():
            flipped += letter.upper()
        else:
            flipped += letter.lower()
    return flipped

def stringify_numbers(numbers):
    string_list = [str(num) for num in numbers]
    joined = "@".join(string_list)
    split_back = joined.split("@")

    return joined, split_back

def calculator(txt):
    left, operator, right = txt.split()

    a = len(left)
    b = len(right)

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '//':
        result = a // b
    else:
        return "wrong operator"

    return '.' * result

def html_end_tag_by_start_tag(start_tag):
    parts = start_tag.split()
    tag_name = parts[0][1:]
    if tag_name[-1] == '>':
        tag_name = tag_name[:-1]

    return f"</{tag_name}>"