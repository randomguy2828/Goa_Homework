def manual_max(lst):
    if not lst:
        return None 

    max_value = lst[0]
    for value in lst[1:]:
        if value > max_value:
            max_value = value
    return max_value

def manual_replace(lst, old_value, new_value):
    for i in range(len(lst)):
        if lst[i] == old_value:
            lst[i] = new_value
    return lst


