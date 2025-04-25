def valid_phone_number(phone_number):
    
    if len(phone_number) != 14:
        return False
    

    if phone_number[0] == '(' and phone_number[4] == ')' and phone_number[5] == ' ' and phone_number[9] == '-':
        try:

            int(phone_number[1:4])  
            int(phone_number[6:9]) 
            int(phone_number[10:]) 
            return True
        except ValueError:
            return False
    
    return False
   

def solution(s):
    pairs = []
    
    for i in range(0, len(s), 2):
        pairs.append(s[i:i+2] if i+1 < len(s) else s[i] + "_")
    
    return pairs