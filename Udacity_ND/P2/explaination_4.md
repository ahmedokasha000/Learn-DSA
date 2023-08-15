# Task 1 - LRU Cache

## Code Design
sort_012 function: This function sorts an array consisting of only 0s, 1s, and 2s using a counting sort approach.

First, it traverses the array once to count the number of 0s, 1s, and 2s. Then, it constructs the sorted array based on these counts.
## Complexity

### Time Complexity

The loop that counts the number of 0s, 1s, and 2s runs in O(n)  where n is the length of the input list.
Constructing the res list also takes O(n) time. Therefore, the overall time complexity of the sort_012 function is O(n).

### Space Complexity

The space complexity is O(n) due to the res list that stores the sorted values. The variables sum_0, sum_1, and sum_2 take up constant space.
