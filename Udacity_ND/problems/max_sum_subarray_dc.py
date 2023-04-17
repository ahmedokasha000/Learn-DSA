# Maximum sum subarray problem with divide and conquer approach


def max_sum_subarray(data_arr):
    """
    Find the maximum sum of a subarray in a given array
    :param data_arr: list of integers
    :return: maximum sum of a subarray
    :rtype: int
    """
    if len(data_arr) == 0:
        return None
    if len(data_arr) == 1:
        return data_arr[0]

    mid = len(data_arr) // 2

    left_max = max_sum_subarray(data_arr[:mid])
    right_max = max_sum_subarray(data_arr[mid:])

    cross_max = max_crossing_subarray(data_arr, mid)

    return max(left_max, right_max, cross_max)


def max_crossing_subarray(data_arr, mid):
    """
    Find the maximum sum of a subarray that crosses the midpoint
    :param data_arr: list of integers
    :type data_arr: list
    :return: maximum sum of a subarray that crosses the midpoint
    :rtype: int
    """

    right_sum = float('-inf')
    cur_sum = 0
    for ind in range(mid+1, len(data_arr)):
        cur_sum += data_arr[ind]
        right_sum = max(right_sum, cur_sum)

    left_sum = float('-inf')
    cur_sum = 0
    for ind in range(mid, -1, -1):
        cur_sum += data_arr[ind]
        left_sum = max(left_sum, cur_sum)
    return left_sum + right_sum


def test_cases_max_sum_subarray():
    assert max_sum_subarray(
        [1, 2, 3, 4, 5]) == 15, f"results are unordered, results = {max_sum_subarray([1, 2, 3, 4, 5])}"
    assert max_sum_subarray(
        [1, -2, 3, 4, -5]) == 7, f"results are unordered,  results = {max_sum_subarray([1, -2, 3, 4, -5])}"
    assert max_sum_subarray([-1, -2, -3, -4, -5]) == - \
        1, f"results are unordered,  results = {max_sum_subarray([-1, -2, -3, -4, -5])}"
    assert max_sum_subarray(
        [1, 2, -3, 4, 5]) == 9, f"results are unordered,  results = {max_sum_subarray([1, 2, -3, 4, 5])}"
    assert max_sum_subarray([1, 2, -3, 4, 5, -6, 7]
                            ) == 10, f"results are unordered,  results = {max_sum_subarray([1, 2, -3, 4, 5, -6, 7])}"


def corner_test_cases_max_sum_subarray():
    assert max_sum_subarray([1]) == 1, f"results are unordered,  results = {max_sum_subarray([1])}"
    assert max_sum_subarray([-1]) == -1, f"results are unordered,  results = {max_sum_subarray([-1])}"
    assert max_sum_subarray([0]) == 0, f"results are unordered,  results = {max_sum_subarray([0])}"
    assert max_sum_subarray([]) == None, f"results are unordered,  results = {max_sum_subarray([])}"


def main():
    test_cases_max_sum_subarray()
    corner_test_cases_max_sum_subarray()


if __name__ == '__main__':
    main()
