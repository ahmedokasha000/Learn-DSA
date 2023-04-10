## The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.

# Here are some examples:

# [0,1] has 0 inversions
# [2,1] has 1 inversion (2,1)
# [3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
# [7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
# The number of inversions can also be thought of in the following manner.

# Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j, if i < j and arr[i] > arr[j] then the pair (i, j) is called an inversion of arr.


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
        return data, 0

    mid_index = len(data) // 2
    left_half = data[:mid_index]
    right_half = data[mid_index:]
    left, left_inv_count = merge_sort(left_half)
    right, right_inv_count = merge_sort(right_half)
    merged_list, inv_count = merge_two_sorted_lists(left, right)
    return merged_list, left_inv_count + right_inv_count + inv_count


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
    print(f"left = {left}, right = {right}")
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            res.append(left[left_ind])
            left_ind += 1
        else:
            res.append(right[right_ind])
            right_ind += 1
    res += left[left_ind:]
    res += right[right_ind:]
    print(f" found {(len(left[left_ind:]) - 1) * left_ind}")
    if (len(left[left_ind:]) - 1) >= 0:
        inversions_count = right_ind + (len(left[left_ind:]) - 1) * right_ind
    else:
        inversions_count = right_ind
    print(f" found {inversions_count} inversions")
    return res, inversions_count

        
def main():
    test_sample = list(range(10))
    shuffle(test_sample)
    print(merge_sort([7, 5, 3, 1]))


    # assert merge_sort(test_sample) == list(range(10000)), "results are unordered"

    # test_sample = []
    # assert merge_sort(test_sample) == [], f"results are unordered, sample = {[]}, results = {test_sample}"


if __name__ == '__main__':
    main()