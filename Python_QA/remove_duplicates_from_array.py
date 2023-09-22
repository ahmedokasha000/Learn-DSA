from typing import List, Tuple

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

def remove_duplicates(nums: List[int]) -> Tuple[int, List[int]]:
    """
    Remove duplicates from a sorted array in-place such that each element
    appears at most twice. Return the new length of the array and the inplace processed array.

    :param nums: The sorted input array.
    :return: The length of the modified array and the modified array.
    :rtype: Tuple[int, List[int]]
    """

    # Initialize read and write pointers to index 1
    read_ptr, write_ptr = 1, 1

    # Initialize count to 1 for counting occurrences of each number
    count = 1

    while read_ptr < len(nums):

        # If the current element is the same as the previous one, increment count
        if nums[read_ptr] == nums[read_ptr - 1]:
            count += 1
        else:
            # Reset count if we encounter a new element
            count = 1

        # If the count is less than or equal to 2, write the element at the write_ptr
        if count <= 2:
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1

        read_ptr += 1

    return write_ptr, nums[:write_ptr]


def test_remove_duplicates():
    """
    Basic test cases for remove_duplicates().
    """
    arr = [1, 1, 1, 2, 2, 3]
    assert remove_duplicates(arr) == (5, [1, 1, 2, 2, 3]), "wrong results for input array [1, 1, 1, 2, 2, 3]"
    arr = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert remove_duplicates(arr) == (7, [0, 0, 1, 1, 2, 3, 3]), "wrong results for input array [0, 0, 1, 1, 1, 1, 2, 3, 3]"


def main():
    test_remove_duplicates()


if __name__ == '__main__':
    main()
