# Task 4 - Dutch National Flag Problem

## Code Design
The sort_012 function sorts an array consisting only of 0s, 1s, and 2s using a single traversal. The algorithm uses three pointers:

end_0_index: Points to the last occurrence of 0 in the sorted part of the array.
start_2_index: Points to the first occurrence of 2 in the sorted part of the array.
cur_index: The current index being evaluated.

## Complexity

### Time Complexity

The loop that counts the number of 0s, 1s, and 2s runs in O(n)  where n is the length of the input list since only single traversal is done

### Space Complexity

The space complexity of the sort_012 function is O(1) (constant space). The function uses a fixed amount of space regardless of the size of the input list, specifically three integer variables to keep track of the indices.
