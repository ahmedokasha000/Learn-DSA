# Longest Common Subsequence¶

# In text analysis, it is often useful to compare the similarity of two texts (imagine if you were trying to determine plagiarism between a source and answer text). In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence (LCS).

# The Longest Common Subsequence is the longest sequence of letters that are present in both the given two strings in the same relative order.

# Example - Consider the two input strings, str1 = 'ABCD' and str2 = 'AXBXDX'. The LCS will be 'ABD' with the length as 3 letters. It is because each of the letters 'A' , 'B', and 'D' are present in both the given two strings in the same relative order. Note that:

# An LCS need not necessarily be a contiguous substring.
# There can be more than one LCS present in the given two strings.
# There can be many more common subsequences present here, with smaller length. But, in this problem we are concerned with the longest common subsequence.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Find the longest common subsequence between two strings.

        :param text1: First string
        :type text1: str
        :param text2: Second string.
        :type text2: str
        :return: Length of the longest common subsequence.
        :rtype: int
        """
        rows = len(text1) + 1
        cols = len(text2) + 1
        lookup = [[0 for _ in range(cols)] for _ in range(rows)]
        for row_ind in range(1, rows):
            for col_ind in range(1, cols):
                if text2[col_ind - 1] == text1[row_ind - 1]:
                    print(f"row_ind: {row_ind}, col_ind: {col_ind}, text1[row_ind - 1]: {text1[row_ind - 1]}, text2[col_ind - 1]: {text2[col_ind - 1]}")
                    lookup[row_ind][col_ind] = lookup[row_ind - 1][col_ind - 1] + 1
                else:
                    print(f"max of {lookup[row_ind][col_ind - 1]} and {lookup[row_ind - 1][col_ind]}")
                    lookup[row_ind][col_ind] = max(lookup[row_ind][col_ind - 1], lookup[row_ind - 1][col_ind])
        print(lookup)
        return lookup[-1][-1]


def test_longest_common_subsequence():
    """ Random test cases for longest common subsequence. Casual test cases, not exhaustive."""
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "abc") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0

def hard_test_longest_common_subsequence():
    """ Hard test cases for longest common subsequence. Extremely large test cases, Corner cases, etc."""
    assert Solution().longestCommonSubsequence("", "") == 0
    assert Solution().longestCommonSubsequence("a", "b") == 0
    assert Solution().longestCommonSubsequence("abcd", "") == 0

    

def main():
    """
    Main function
    """
    #test_longest_common_subsequence()
    #hard_test_longest_common_subsequence()
    Solution().longestCommonSubsequence("abcba", "abcbcba")
    print("Main function")
    
if __name__ == '__main__':
    # Call Main
    main()