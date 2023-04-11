import math
from random import shuffle
import random


def fast_select(data, k):
    """
    Returns the kth smallest element in the given unsorted list.
    :param data: The list of numbers to search for the kth smallest element.
    :type data: list
    :param k: The index of the desired element in the sorted list.
    :type k: int
    :return: The kth smallest element in the given list.
    :rtype: int or float
    """

    if len(data) == 1:
        return data[0]

    # Calculate the number of groups of 5 elements in the list
    n_over_5_groups = math.ceil(len(data) / 5)

    # Find the median of each group of 5 elements
    n_over_5_medians = []
    for i in range(n_over_5_groups):
        start = i * 5
        end = (start + 5) if (start + 5) < len(data) else len(data)
        group_median = median_sorted(sorted(data[start:end]))
        n_over_5_medians.append(group_median)

    # Use fast_select recursively to find the pivot
    if (len(n_over_5_medians) == 1):            # Base case for this task
        pivot = n_over_5_medians[0]
    else:
        pivot = fast_select(n_over_5_medians, len(data) // 10)
    # Partition the list into three groups around the pivot
    smaller_array, greater_array, equals_array = [], [], []
    for element in data:
        if element < pivot:
            smaller_array.append(element)
        elif element > pivot:
            greater_array.append(element)
        else:
            equals_array.append(element)

    # Recurse on the appropriate group of elements
    if k <= len(smaller_array):
        return fast_select(smaller_array, k)
    elif k > len(smaller_array) + len(equals_array):
        return fast_select(greater_array, k - len(smaller_array) - len(equals_array))
    else:
        return pivot



def fast_select2(data, k):
    """
    This function returns the k-th smallest number from the given unsorted list of integers using the quickselect algorithm.
    If the list has only one element, it returns that element.
    :param data: An unsorted list of integers.
    :param k: An integer k which specifies the k-th smallest number to be returned from the list.
    :return: The k-th smallest number from the list.
    """
    # Check if the list has only one element
    if len(data) == 1:
        return data[0]

    # Select a random pivot
    pivot = random.choice(data)

    # Initialize three arrays to store elements smaller, greater and equal to pivot
    smaller_array, greater_array, equals_array = [], [], []

    # Iterate through each element in the list and append it to appropriate array
    for element in data:
        if element < pivot:
            smaller_array.append(element)
        elif element > pivot:
            greater_array.append(element)
        else:
            equals_array.append(element)

    # If k is less than the length of smaller_array, recursively call the function with smaller_array and k
    if k < len(smaller_array):
        return fast_select2(smaller_array, k)

    # If k is greater than or equal to the sum of length of smaller_array and equals_array, recursively call the function with greater_array and k
    elif k >= len(smaller_array) + len(equals_array):
        return fast_select2(greater_array, k - len(smaller_array) - len(equals_array))

    # If k is between length of smaller_array and sum of length of smaller_array and equals_array, return the pivot
    else:
        return pivot


def median_sorted(data):

    if len(data) % 2 == 0:
        return (data[len(data) // 2] + data[(len(data) // 2) - 1]) / 2
    else:
        return data[len(data) // 2]


def test_cases_fast_select():
    test_sample = list(range(100))
    shuffle(test_sample)
    assert fast_select(
        test_sample, 1) == 0, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 1)}"
    assert fast_select(
        test_sample, 2) == 1, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 2)}"
    assert fast_select(
        test_sample, 3) == 2, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 3)}"
    assert fast_select(
        test_sample, 4) == 3, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 4)}"
    assert fast_select(
        test_sample, 5) == 4, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 5)}"
    assert fast_select(
        test_sample, 6) == 5, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 6)}"
    assert fast_select(
        test_sample, 7) == 6, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 7)}"
    assert fast_select(
        test_sample, 8) == 7, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 8)}"
    assert fast_select(
        test_sample, 9) == 8, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, 9)}"


def random_test_cases_fast_select():
    for i in range(100):
        test_sample = list(range(100))
        shuffle(test_sample)
        assert fast_select(
            test_sample, i) == i, f"results are unordered, sample = {test_sample}, results = {fast_select(test_sample, i)}"


def main():
    test_cases_fast_select()
    # random_test_cases_fast_select()


if __name__ == '__main__':
    main()
