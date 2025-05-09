def cakes(recipe, available):
    return min(available.get(ingredient, 0) // amount for ingredient, amount in recipe.items())

def first_non_repeating_letter(s):
    lower_s = s.lower()
    
    for char in s: 
        if lower_s.count(char.lower()) == 1:
            return char 
    
    return "" 
