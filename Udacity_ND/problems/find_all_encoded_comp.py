# Problem statement¶
# In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on, find out all the codes that are possible for a given input number.

# Example 1

# number = 123
# codes_possible = ["aw", "abc", "lc"]
# Explanation: The codes are for the following number:

# 1 . 23 = "aw"
# 1 . 2 . 3 = "abc"
# 12 . 3 = "lc"
# Example 2

# number = 145
# codes_possible = ["ade", "ne"]
# Return the codes in a list. The order of codes in the list is not important.

# Note: you can assume that the input number will not contain any 0s

import string

mapp_dict = {str(i+1):string.ascii_lowercase[i] for i in range(26)}


def all_codes(num):
    number = str(num)
    if len(number) == 1:
        return [mapp_dict[number[0]]]
    elif len(number) > 1:
        res = []
        if mapp_dict.get(number[0:2]):
            comps = [mapp_dict[number[0:2]] + comp for comp in all_codes(number[2:])]
            res.extend(comps)
        comps = [mapp_dict[number[0:1]] + comp for comp in all_codes(number[1:])]
        res.extend(comps)    
        return res
    else:
        return ['']
    
    
def main():
    print(all_codes(123))
    print(all_codes(11))
    print(all_codes(1))
    
if __name__ == '__main__':
    main()