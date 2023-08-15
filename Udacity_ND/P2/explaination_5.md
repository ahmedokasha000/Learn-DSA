# Task 1 - Autocomplete with Tries

## Code Design

**TrieNode class:** Represents a node in the trie. Each node has a flag is_word to indicate if it's the end of a word and a dictionary children to store its child nodes. The suffixes method is a recursive function that collects all the suffixes for complete words below the current node.

**Trie class:** Represents the trie structure. It provides methods to:

- insert: Add a word to the trie.
- exists: Check if a word exists in the trie.
- startsWith: Check if there's any word in the trie that starts with a given prefix.
- find: Find the node in the trie that represents a given prefix.

## Complexity

### Time Complexity

- insert method: O(k), where k is the length of the word. This is because it traverses the word once.

- exists method: O(k), where k is the length of the word. Similar reasoning as the insert method.

- startsWith method: O(k), where k is the length of the prefix.

- find method: O(k), where k is the length of the prefix.

- suffixes method: In the worst case, it can be O(n), where n is the total number of nodes in the trie.

### Space Complexity

TrieNode class: O(c), where c is the number of children. In the worst case, if every letter is unique, c can be equal to the total number of letters across all words.

Trie class: O(n×k), where n is the number of words and k is the average length of a word.