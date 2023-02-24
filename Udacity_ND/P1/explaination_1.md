# Task 1 - LRU Cache

## Code Design

An ordered dictionary is utilized in the implementation of this LRU cache because it enables constant-time access to its items. Additionally, the use of an ordered dictionary eliminates the need for creating a new double linked list to maintain the order of added items, as the ordered dictionary inherently preserves the order of insertion.

## Complexity

### Time Complexity

The time complexity for the get() and set() operations of this LRU cache implementation is O(1). This is because the use of an ordered dictionary allows for constant time access and deletion of items by key.

### Space Complexity

The space complexity is also O(n), where n is the capacity of the cache, since the cache can store up to n key-value pairs.
