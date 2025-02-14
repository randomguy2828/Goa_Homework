def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
def expression_matter(a, b, c):
    return max(a + b + c, a * b * c, (a + b) * c, a * (b + c), a + b * c, a * b + c)

def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)

def how_much_i_love_you(nb_petals):
    phrases = [
        "I love you", "a little", "a lot", "passionately",
        "madly", "not at all"
    ]
    index = (nb_petals - 1) % len(phrases)
    return phrases[index]

def reverse_list(l):
    return l[::-1]

def odd_count(n):
    return n // 2

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

def two_sort(array):
    return '***'.join(sorted(array)[0])