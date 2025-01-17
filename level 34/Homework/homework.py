def rental_car_cost(d):
    daily_cost = 40
    total_cost = daily_cost * d
    
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20

    return total_cost

def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    
def remove_exclamation_marks(s):
    return s.replace('!', '')

def points(games):
    total_points = 0
    for game in games:
        x, y = map(int, game.split(':')) 
        if x > y:
            total_points += 3 
        elif x == y:
            total_points += 1
    return total_points

def get_volume_of_cuboid(length, width, height):
     return length * width * height

def area_or_perimeter(l, w):
    return l * w if l == w else 2 * (l + w)

def set_alarm(employed, vacation):
     return employed and not vacation

def sum_mix(arr):
     return sum(int(x) for x in arr)

def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    return sum(arr) - max(arr) - min(arr)