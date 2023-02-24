
# Task 2 - File Recursion

## Code Design

The program uses a recursive function to traverse all subdirectories and search for specific files. The function's base case is that the current directory is a file. If this is the case, the file will be added to the search results or not, depending on whether its file extension matches the specified suffix.

## Complexity

### Time Complexity

The time complexity of this function is proportional to the number of files and directories within it, including any subdirectories, and is represented as O(n).

### Space Complexity

The space complexity is also O(n), where n is number of files ends with required suffix.

