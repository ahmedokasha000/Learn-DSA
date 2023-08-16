def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    end_0_index = -1
    start_2_index = len(input_list)
    cur_index = 0
    while cur_index < start_2_index:
        if input_list[cur_index] == 0:
            input_list[end_0_index + 1], input_list[cur_index] = input_list[cur_index],  input_list[end_0_index + 1]
            cur_index += 1
            end_0_index += 1
        elif input_list[cur_index] == 1:
            cur_index += 1
        else:
            input_list[start_2_index - 1], input_list[cur_index] = input_list[cur_index],  input_list[start_2_index - 1]
            start_2_index -= 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


def test_sort_012():
    """
    Using test_function for testing different test cases and corner scenarios.
    """
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2])
    test_function([])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
    test_function([2, 2, 2, 2, 2, 2, 1, 1, 1, 1])
    test_function([1, 1, 1, 1, 1, 1, 2, 2, 2, 2])
    test_function([0, 0, 0, 0, 0, 0, 2, 2, 2, 2])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])


def main():
    test_sort_012()


if __name__ == '__main__':
    main()
