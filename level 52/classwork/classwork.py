def move_zeros(lst):
    no_zero = list(filter(lambda x: x != 0 or x is False, lst))
    zero_num = len(lst) - len(no_zero)
    return no_zero + [0] * zero_num

def generate_hashtag(s):
    if not s or len(s.strip()) == 0:
        return False
    Hash = '#' + ''.join(word.capitalize() for word in s.split())
    return Hash if len(Hash) <= 140 else False