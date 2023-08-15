# Task 3 - Rearrange Array Digits

## Code Design

quick_sort function: Implements the Quick Sort algorithm using the last element as the pivot. It partitions the list into two: elements less than or equal to the pivot and elements greater than the pivot. It then recursively sorts these partitions.

rearrange_digits function: Rearranges the digits of the input list to form two numbers with a maximized sum. It sorts the input list using quick_sort and constructs the two numbers by alternately taking the largest available digit.


## Complexity

### Time Complexity

quick_sort function: The average time complexity of Quick Sort is O(n log n) where n is the number of elements in the list. However, in the worst case (when the list is already sorted or reverse sorted), the time complexity can be O(n^^2). This worst-case scenario can be avoided by using a randomized pivot or the median of three method, but the provided code uses the last element as the pivot.

rearrange_digits function: The time complexity is dominated by the quick_sort function, so it's O(n log n).  The while loop that constructs the two numbers runs in O(n) time, but this is overshadowed by the sorting step.

### Space Complexity

quick_sort function: The space complexity is O(n) because of the smaller_array and greater_array lists that are created during each recursive call. In the worst case, the recursion depth can be O(n) leading to a space complexity of O(n^^2). However, in practice, the average space complexity is much less than O(n^^2) due to the division of the list.

rearrange_digits function: The space complexity is dominated by the quick_sort function, so it's O(n) on average. The variables first_num and second_num take up constant space.