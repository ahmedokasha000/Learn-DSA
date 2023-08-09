def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    last_0_index = -1
    res = []
    for val in input_list:
        if val == 2:
            res.append(val)
        else:
            res.insert(last_0_index + 1, val)
        if val == 0:
            last_0_index += 1
    return res


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


def test_sort_012():
    assert sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) == [0, 0, 0, 1, 1, 1, 2, 2, 2, 2,
                                                           2], f"results are unordered, results = {sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])}"
    assert sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2]) == [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2,
                                                              2], f"results are unordered, results = {sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2])}"
    assert sort_012([]) == [], f"results are unordered, results = {sort_012([])}"
    assert sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1], f"results are unordered, results = {sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])}"
    assert sort_012([2, 2, 2, 2, 2, 2, 1, 1, 1, 1]) == [1, 1, 1, 1, 2, 2, 2, 2, 2, 2], f"results are unordered, results = {sort_012([2, 2, 2, 2, 2, 2, 1, 1, 1, 1])}"

def main():
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_sort_012()


if __name__ == '__main__':
    main()
