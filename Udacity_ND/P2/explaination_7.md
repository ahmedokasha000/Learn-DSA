# Task 1 - HTTPRouter using a Trie

## Code Design

**RouteTrieNode class:** Represents a node in the trie. Each node has a handler (defaulted to None) and children, which are stored in a dictionary.

**RouteTrie class:** Represents the trie structure. It has methods to add a path and its associated handler and to find a handler given a path.

**Router class:** Wraps around the RouteTrie. It provides a higher-level interface for adding handlers for paths and looking up handlers for given paths. It also handles paths that are not found in the trie by returning a "not found" handler.

## Complexity

### Time Complexity

**add method (in RouteTrie):** O(k) where k is the number of directories in the path. This is because it traverses the path once.
**find method (in RouteTrie):** O(k), where k is the number of directories in the path.

**add_handler method (in Router):** O(k), as it's dominated by the time complexity of the add method in RouteTrie.

**lookup method (in Router):** O(k), as it's dominated by the time complexity of the find method in RouteTrie.

### Space Complexity

**RouteTrieNode class:** O(c), where c is the number of children.

**RouteTrie class:** O(n×k), where n is the number of paths and k is the average number of directories in a path.

**Router class:** The space complexity is dominated by the RouteTrie, so it's O(n×k).