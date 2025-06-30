def split_on_a(sentence):
    return sentence.split("a")

def join_with_star(string_list):
    return '*'.join(string_list)

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    count_positives = sum(1 for x in arr if x > 0)
    sum_negatives = sum(x for x in arr if x < 0)
    
    return [count_positives, sum_negatives]

def print_array(arr):
    result = ""
    for i in range(len(arr)):
        result += str(arr[i])
        if i < len(arr) - 1:
            result += ","
    return result

def split_in_parts(s, part_length):
    result = []
    
    for i in range(0, len(s), part_length):
        part = s[i:i+part_length]
        result.append(part)
    
    return ' '.join(result)

