import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)
    min_val = max_val = ints[0]

    for var in ints:
        min_val = var if var < min_val else min_val
        max_val = var if var > max_val else max_val
    return (min_val, max_val)


def test_cases_get_min_max():
    """ diverse test cases for get_min_max() """
    test_case = [i for i in range(0, 10)]
    random.shuffle(test_case)
    print("Pass" if ((0, 9) == get_min_max(test_case)) else "Fail")

    test_case = [i for i in range(0, 100)]
    random.shuffle(test_case)
    print("Pass" if ((0, 99) == get_min_max(test_case)) else "Fail")

    test_case = [i for i in range(0, 1000)]
    random.shuffle(test_case)
    print("Pass" if ((0, 999) == get_min_max(test_case)) else "Fail")

    test_case = [i for i in range(-100000, 10000)]
    random.shuffle(test_case)
    print("Pass" if ((-100000, 9999) == get_min_max(test_case)) else "Fail")

    test_case = [i for i in range(-1000000, 1000000)]
    random.shuffle(test_case)
    print("Pass" if ((-1000000, 999999) == get_min_max(test_case)) else "Fail")

    test_case = []
    random.shuffle(test_case)
    print("Pass" if ((None, None) == get_min_max(test_case)) else "Fail")

    test_case = [5]
    random.shuffle(test_case)
    print("Pass" if ((5, 5) == get_min_max(test_case)) else "Fail")


def main():
    test_cases_get_min_max()


if __name__ == '__main__':
    main()
