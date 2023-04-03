
from random import shuffle
import time


def merge_sort(data: list):
    """
    Sorts a list of integers using the merge sort algorithm.
    
    :param data: A list of integers to be sorted.
    :type data: list
    :return: A sorted list of integers.
    :rtype: list
    """
    if len(data) <= 1:
        return data

    mid_index = len(data) // 2
    left_half = data[:mid_index]
    right_half = data[mid_index:]

    left, right = merge_sort(left_half), merge_sort(right_half)

    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(left, right):
    """
    Merges two sorted lists of integers into a single sorted list.
    
    :param left: A sorted list of integers.
    :type left: list
    :param right: A sorted list of integers.
    :type right: list
    :return: A single sorted list containing all integers from both input lists.
    :rtype: list
    """
    res = []
    left_ind = right_ind = 0
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            res.append(left[left_ind])
            left_ind += 1
        else:
            res.append(right[right_ind])
            right_ind += 1
    res += left[left_ind:]
    res += right[right_ind:]
    return res

        
def main():
    test_sample = list(range(10000))
    shuffle(test_sample)


    assert merge_sort(test_sample) == list(range(10000)), "results are unordered"

    test_sample = []
    assert merge_sort(test_sample) == [], f"results are unordered, sample = {[]}, results = {test_sample}"


if __name__ == '__main__':
    main()