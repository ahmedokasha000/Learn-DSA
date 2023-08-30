import collections

import numpy as np

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack. Solving the knapsack problem using dynamic programming.

    :param knapsack_max_weight: the maximum weight the knapsack can hold
    :type knapsack_max_weight: int
    :param items: list of items to place in the knapsack
    :type items: List[Item]
    """
    rows = len(items) + 1
    cols = knapsack_max_weight + 1
    items = [0] + items
    lookup = np.zeros((rows, cols)).astype(int)
    for row_ind in range(1, rows):
        for col_ind in range(1, cols):
            if col_ind < items[row_ind].weight:
                lookup[row_ind, col_ind] = lookup[row_ind - 1, col_ind]
            else:
                lookup[row_ind, col_ind] = max(lookup[row_ind - 1, col_ind], lookup[row_ind - 1,
                                               col_ind - items[row_ind].weight] + items[row_ind].value)

    return lookup[-1, -1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])
