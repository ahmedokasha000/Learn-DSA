

def search_rotated_array(array, target):
    """
    Find the index by searching in a rotated sorted array.
    :param array: Input array to search
    :type array: List
    :param target: Target to search for
    :type target: int
    :return: Index or -1
    :rtype: int
    """
    res = __search_rotated_sorted_array(array, target, 0, len(array) - 1)
    return res


def __search_rotated_sorted_array(array, target, start, end):
    """
    Find the index by searching in a rotated sorted array. Customized fast selection recursive function.
    :param array: Input array to search
    :type array: List
    :param target: Target to search for
    :type target: int
    :param start: Start index
    :type start: int
    :param end: End index
    :type end: int
    :return: Index or -1
    :rtype: int
    """

    # Base cases for recursion

    # empty array
    if start > end:
        return -1
    # single element array
    if start == end:
        return start if array[start] == target else -1
    mid_index = (start + end) // 2
    # value found in the middle
    if array[mid_index] == target:
        return mid_index

    left_end = mid_index - 1 if mid_index - 1 >= 0 else 0
    right_start = mid_index + 1

    # check if the left half is sorted
    if array[start] <= array[left_end]:
        if target >= array[start] and target <= array[left_end]:
            return __search_rotated_sorted_array(array, target, start, left_end)
        else:
            return __search_rotated_sorted_array(array, target, right_start, end)
    # check if the right half is sorted
    if array[right_start] <= array[end]:
        if target >= array[right_start] and target <= array[end]:
            return __search_rotated_sorted_array(array, target, right_start, end)
        else:
            return __search_rotated_sorted_array(array, target, start, left_end)


def test_search_rotated_array_basic():
    assert search_rotated_array([6, 8, 9, 0, 1, 2, 3, 4, 5], 6) == 0, f"results are unordered, results = {search_rotated_array([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)}"
    assert search_rotated_array([6, 7, 8, 9, 10, 1, 2, 3, 4], 1) == 5, f"results are unordered, results = {search_rotated_array([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)}"
    assert search_rotated_array([6, 7, 8, 1, 2, 3, 4], 8) == 2, f"results are unordered, results = {search_rotated_array([6, 7, 8, 1, 2, 3, 4], 8)}"
    assert search_rotated_array([6, 7, 8, 1, 2, 3, 4], 1) == 3, f"results are unordered, results = {search_rotated_array([6, 7, 8, 1, 2, 3, 4], 1)}"


def test_random_array_cases():
    assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0) == 4, f"results are unordered, results = {search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0)}"
    assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3) == -1, f"results are unordered, results = {search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3)}"


def test_corner_cases():
    assert search_rotated_array([], 1) == -1, f"results are unordered, results = {search_rotated_array([], 1)}"
    assert search_rotated_array([1], 1) == 0, f"results are unordered, results = {search_rotated_array([1], 1)}"
    assert search_rotated_array([1], 2) == -1, f"results are unordered, results = {search_rotated_array([1], 2)}"
    assert search_rotated_array([1, 2], 1) == 0, f"results are unordered, results = {search_rotated_array([1, 2], 1)}"
    assert search_rotated_array([1, 2], 2) == 1, f"results are unordered, results = {search_rotated_array([1, 2], 2)}"
    assert search_rotated_array([1, 2], 3) == -1, f"results are unordered, results = {search_rotated_array([1, 2], 3)}"


def main():
    # assert search_rotated_array([1, 2], 2) == 1, f"results are unordered, results = {search_rotated_array([1, 2], 2)}"

    test_search_rotated_array_basic()
    test_random_array_cases()
    test_corner_cases()


if __name__ == '__main__':
    main()