# Task 6 - Union and Intersection

## Code Design
Two iterative functions are implemented to traverse the two lists only once. During the traversal, specific values are stored in a hash table (set) to facilitate faster access when required. Additionally, the output list is calculated during the iteration to prevent duplicating the computational complexity.

## Complexity

### Time Complexity

#### Union

assuming length of first list is n and second is m

1. Iterating over the first list is of complexity O(n)
2. Adding and checking values in `union_vals` set (hash table) is of complexity O(1)
3. Iterating over the second list is of complexity O(m)

Final complexity is of `O(n+m)` where n, m are the size of the two lists.


#### Intersection

assuming length of first list is **n** and second is **m**:

1. Iterating over the first list is of complexity O(n)
2. Adding and checking values in `l1_values` , `intersec_vals` sets (hash table) is of complexity O(1)
3. Iterating over the second list is of complexity O(m)

Final complexity is of `O(n+m)` where n, m are the size of the two lists.

### Space Complexity

#### Union

assuming length of first list is n and second is m

1. While iterating over the first list, we store its elements in `union_vals` which is of complexity O(n)
2. While iterating over the second, we store its elements in `union_vals` which is of complexity O(m)

Final complexity is of `O(n+m)` where n, m are the size of the two lists.

#### Intersection

assuming length of first list is n and second is m

1. While iterating over the first list, we store its elements in `l1_values` which is of complexity O(n)
2. While iterating over the first list , we store its elements in `intersec_vals` which can be of complexity O(m)

Final complexity is of `O(n+m)` where n, m are the size of the two lists.
