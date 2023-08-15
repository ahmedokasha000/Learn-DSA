import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_val = max_val = ints[0]

    for var in ints:
        min_val = var if var < min_val else min_val
        max_val = var if var > max_val else max_val
    return (min_val, max_val)


### Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
