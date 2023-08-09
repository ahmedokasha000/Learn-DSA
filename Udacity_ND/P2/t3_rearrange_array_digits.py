
def quick_sort(data: list):
    """
    Quick sort algorithm for sorting a list of integers.
    :param data: Input list to be sorted
    :type data: List
    :return: Sorted list of integers
    :rtype: List
    """
    if len(data) <= 1:
        return data

    smaller_array, greater_array = [], []

    pivot = data[-1]
    for element in data[:-1]:
        if element <= pivot:
            smaller_array.append(element)
        else:
            greater_array.append(element)

    return quick_sort(smaller_array) + [pivot] + quick_sort(greater_array)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = quick_sort(input_list)
    first_num = 0
    second_num = 0
    while len(sorted_list) > 0:
        first_num = first_num * 10 + sorted_list.pop()
        if len(sorted_list) > 0:
            second_num = second_num * 10 + sorted_list.pop()
    return first_num, second_num

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]