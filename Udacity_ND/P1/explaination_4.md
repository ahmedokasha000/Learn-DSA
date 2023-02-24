
# Task 4 - Active Directory

## Code Design
A recursive function is implemented to traverse all sub groups while checking users in these groups. The base case is reached once we find the user, in that case we will return and stop traversing other groups.

## Complexity

### Time Complexity
O(n) where n is the number of all sub groups and the users inside.
### Space Complexity

Complexity = O(1). We don't have to store variables. however the space for storing stack frames will increase when the recursion depth increase.

