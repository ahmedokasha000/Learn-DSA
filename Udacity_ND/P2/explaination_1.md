# Task 1 - Square Root of an Integer

## Code Design
This code uses binary search to find the integer square root of a given number. The idea is to keep narrowing down the search space by half until the correct integer square root is found.

## Complexity

### Time Complexity
The time complexity of the solution is same as time complexity of binary search which is O(log n) since computation is cut down to half after each iteration.

### Space Complexity

The space complexity of the find_sqrt function is determined by the recursive call stack. In the worst case, the depth of the recursion is O(log n)