# Task 1 - LRU Cache

## Code Design

An ordered dictionary is utilized in the implementation of this LRU cache because it enables constant-time access to its items. Additionally, the use of an ordered dictionary eliminates the need for creating a new double linked list to maintain the order of added items, as the ordered dictionary inherently preserves the order of insertion.

## Complexity

### Time Complexity

The time complexity for the get() and set() operations of this LRU cache implementation is O(1). This is because the use of an ordered dictionary allows for constant time access and deletion of items by key.

### Space Complexity

The space complexity is also O(n), where n is the capacity of the cache, since the cache can store up to n key-value pairs.

# Task 2 - File Recursion

## Code Design

The program uses a recursive function to traverse all subdirectories and search for specific files. The function's base case is that the current directory is a file. If this is the case, the file will be added to the search results or not, depending on whether its file extension matches the specified suffix.

## Complexity

### Time Complexity

The time complexity of this function is proportional to the number of files and directories within it, including any subdirectories, and is represented as O(n).

### Space Complexity

The space complexity is also O(n), where n is number of files ends with required suffix.


# Task 3 - Huffman Coding

## Code Design

To implement Huffman encoding, we first create a node class for the Huffman tree, which is later used as a building block for a priority queue and the Huffman tree itself. We then implement a priority queue to enable faster access to the minimum node and faster insertion of new Huffman nodes. Next, we build the Huffman tree according to the Huffman tree definition. We then traverse the entire tree recursively to create a hashmap for the Huffman codes. Finally, with the Huffman code hashmap and Huffman tree in place, data can be easily encoded and decoded.

## Complexity

### Time Complexity

#### Encoding

Complexity = O(n log n).

This is because the process of creating a Huffman encoding involves several steps:

1. First, creating a hashmap of letter occurrences takes O(n) time.
2. Then, iterating over each character occurrence and inserting them into a priority queue takes O(n log n) time.
3. Extracting all items from the priority queue also takes O(n log n) time.
4. Creating a hashmap for the Huffman code from the tree takes O(n) time.
5. Finally, encoding the data itself takes O(n) time.

#### Decoding

Complexity = O(n).

We iterate over the encoded data only once.

### Space Complexity

Complexity = O(n).

No operation is taking space more than the length of input data for both encoding or decoding.


# Task 4 - Active Directory

## Code Design
A recursive function is implemented to traverse all sub groups while checking users in these groups. The base case is reached once we find the user, in that case we will return and stop traversing other groups.

## Complexity

### Time Complexity
O(n) where n is the number of all sub groups and the users inside.
### Space Complexity

Complexity = O(1). We don't have to store variables. however the space for storing stack frames will increase when the recursion depth increase.

# Task 5 - Block chain

## Code Design
The code creates a Block class that includes all necessary attributes, including a reference to the previous block if exists. Then, a data structure is established to represent the blockchain, which is similar to a singly linked list, except that the tail of the chain is kept, and each block has a link to the previous one.

## Complexity

### Time Complexity
- O(1) for insertion and pop operations.
- O(n) searching, replace, or delete.
### Space Complexity

Complexity = O(n).

# Task 6 - Union and Intersection

## Code Design
Two iterative functions are implemented to traverse the two lists only once. During the traversal, specific values are stored in a hash table (set) to facilitate faster access when required. Additionally, the output list is calculated during the iteration to prevent duplicating the computational complexity.

## Complexity

### Time Complexity
- O(n+m) where n, m are the size of the two lists. Complexity is same for intersection and union.
### Space Complexity

- O(2(n+m)) which will end up with O(n+m). since we are using a hash table for storing some of these values. Results are almost the same for both union and intersection.