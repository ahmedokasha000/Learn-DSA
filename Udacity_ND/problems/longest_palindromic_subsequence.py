

def longest_palindromic_subsequence(text: str) -> int:
    """
    Calculate the length of the longest palindromic subsequence in a given string.

    :param text: Input string
    :type text: str
    :return: Length of the longest palindromic subsequence.
    :rtype: int
    """
    cols = len(text)
    rows = len(text)
    lookup = [[0] * cols for _ in range(rows)]

    for i in range(cols):
        lookup[i][i] = 1

    for row_ind in range(rows - 1, -1, -1):
        for col_ind in range(row_ind + 1, cols):
            if text[row_ind] == text[col_ind]:
                lookup[row_ind][col_ind] = lookup[row_ind + 1][col_ind - 1] + 2
            else:
                lookup[row_ind][col_ind] = max(lookup[row_ind + 1][col_ind], lookup[row_ind][col_ind - 1])

    return lookup[0][cols - 1]


def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1


def main():
    test_longest_palindromic_subsequence()


if __name__ == '__main__':
    # Call Main
    main()
