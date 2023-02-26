
# Task 4 - Active Directory

## Code Design
A recursive function is implemented to traverse all sub groups while checking users in these groups. The base case is reached once we find the user, in that case we will return and stop traversing other groups.

## Complexity

### Time Complexity

At worst case, when number of groups is n a m users is n:

1. First, we will need to go through all groups, which is of complexity of O(n).
2. In each group, we will check if the user exist in the users set(hash table) which is of complexity of O(1)

In the end complexity O(n) where n is the number of all groups.

### Space Complexity

1. For `Group` class space complexity O(n * m) where n is number of groups ad m is number of users inside.
2. For `is_user_function` space complexity **O(1)** since we don't need to store anything. However the space for storing stack frames will increase when the recursion depth increases. As a result we can say that space complexity is of **O(d)** where d is the depth of call stack if call stack is taken into consideration.
