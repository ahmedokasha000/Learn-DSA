# Task 6 - Max and Min in a Unsorted Array

## Code Design

get_min_max function: This function returns a tuple containing the minimum and maximum values from a list of integers. It works by traversing the list once, updating min_val and max_val whenever it encounters a smaller or larger value, respectively.

## Complexity

### Time Complexity

The loop that checks each integer in the list runs in O(n) time, where n is the length of the input list ints. Therefore, the overall time complexity of the get_min_max function is O(n).

### Space Complexity

The space complexity is O(1) (constant space) because the function uses a fixed amount of space regardless of the size of the input list. Specifically, it uses two variables, min_val and max_val, to store the minimum and maximum values, and these take up constant space.
