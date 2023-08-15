# Task 2 - Search Rotated Sorted Array

## Code Design
__search_rotated_sorted_array is a recursive function that performs Customized fast selection recursively on the rotated sorted array. The function first checks for base cases (empty array or single-element array). Then, it checks if the target is the middle element. If not, it determines which half of the array is sorted and then checks if the target lies within that half. Depending on the result, it either searches the left or the right half of the array.

## Complexity
The algorithm uses a modified binary search. In the worst case, the binary search will be called recursively on half of the array. Thus, the time complexity is O(log n) where n is the length of the array.
### Time Complexity


### Space Complexity

The space complexity is determined by the depth of the recursive call stack. In the worst case, the depth of the recursion is O(log n) so the space complexity is also O(log n).