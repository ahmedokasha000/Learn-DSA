
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

