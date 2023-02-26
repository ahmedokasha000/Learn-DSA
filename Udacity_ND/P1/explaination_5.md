# Task 5 - Block chain

## Code Design
The code creates a Block class that includes all necessary attributes, including a reference to the previous block if exists. Then, a data structure is established to represent the blockchain, which is similar to a singly linked list, except that the tail of the chain is kept, and each block has a link to the previous one.

## Complexity

### Time Complexity
- O(1) for block chain **insertion** and **pop** operations since we will be adding to the end and accessing the last element.
- O(n) searching, replace, or delete since we need to iterate over the block chanin.
- O(n) for `len` function.
### Space Complexity

To create and store a block chain we will need to create **n** `Block` making complexity O(n).