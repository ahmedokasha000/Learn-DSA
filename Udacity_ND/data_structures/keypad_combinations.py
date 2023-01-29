def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(number):
    '''
    getting all possible combinations for pressing
    keypad numbers in sequence.
    '''
    num= str(number)
    result_combinations = []
    
    if len(num) != 0:
        first_num = int(num[0])
        rest = num[1:]
        next_combs = keypad(rest)
        for comb in next_combs:
            for ch in get_characters(first_num):
                new_comp = ch + comb
                result_combinations.append(new_comp)
        if len(next_combs) == 0:
            for ch in get_characters(first_num):
                new_comp = ch
                result_combinations.append(new_comp)
        
    return result_combinations
    
keypad(23)
keypad(0)
keypad(12)