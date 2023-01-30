# Problem Statement
# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

# Example 1:

# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.
# Example 2:

# arr = [1, 2, -5, -4, 1, 6]
# The largest sum is 7, which is the sum of the last two elements of the array.


# arr = [-11, -2, -5, -4, -1, -6]
# The largest sum is -1, which is the sum of the last two elements of the array.
## Algorithm used : Kadane's Algorithm 


def max_sum_subarray(array):
    print(f" array = {array}")
    max_sum = current_sum = array[0]
    for val in array[1:]:
        current_sum = max(current_sum + val, val)
        max_sum = max(current_sum, max_sum)
        print(f" new value = {val} current sum = {current_sum} max sum = {max_sum}")

    return max_sum



def main():
    arr0 =  [5, 2, 3, -4, 6]
    arr1 =  [1, 2, 3, -4, 6]
    arr2 =  [1, 2, 3, -4, -6, 1, 2, 2]
    arr3 =  [-4, -8, 2, -4, -5]
    arr4 =  [-4, -8, -2, -4, -5]
    assert max_sum_subarray(arr0) == 12, "failed arr0"
    assert max_sum_subarray(arr1) == 8, "failed arr1"
    assert max_sum_subarray(arr2) == 6, "failed arr2"
    assert max_sum_subarray(arr3) == 2, "failed arr3"
    assert max_sum_subarray(arr4) == -2, "failed arr4"
    
if __name__ == '__main__':
    main()