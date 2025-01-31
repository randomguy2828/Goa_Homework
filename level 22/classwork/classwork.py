def remove_exclamation_marks(s):
     return s.replace('!', '')

def update_light(current):
    light = ['red', 'yellow', 'green']
    if current == light[1]:
        return light[0]
    elif current == light[2]:
        return light[1]
    return light[2]

def set_alarm(employed, vacation):
     return employed and not vacation

def get_average(marks):
    total_sum = sum(marks)
    average = total_sum // len(marks)
    return average

def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    if n < 10:
        return "Keep at it until you get it"
    input(n)
