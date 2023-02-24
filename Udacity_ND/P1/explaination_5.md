# Task 5 - Block chain

## Code Design
The code creates a Block class that includes all necessary attributes, including a reference to the previous block if exists. Then, a data structure is established to represent the blockchain, which is similar to a singly linked list, except that the tail of the chain is kept, and each block has a link to the previous one.

## Complexity

### Time Complexity
- O(1) for insertion and pop operations.
- O(n) searching, replace, or delete.
### Space Complexity

Complexity = O(n).

