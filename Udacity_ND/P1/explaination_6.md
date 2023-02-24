# Task 6 - Union and Intersection

## Code Design
Two iterative functions are implemented to traverse the two lists only once. During the traversal, specific values are stored in a hash table (set) to facilitate faster access when required. Additionally, the output list is calculated during the iteration to prevent duplicating the computational complexity.

## Complexity

### Time Complexity
- O(n+m) where n, m are the size of the two lists. Complexity is same for intersection and union.
### Space Complexity

- O(2(n+m)) which will end up with O(n+m). since we are using a hash table for storing some of these values. Results are almost the same for both union and intersection.