# Problem Statement
# Given an integer array, find and return all the subsets of the array. The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

# Note:

# An empty set will be represented by an empty list.
# If there are repeat integers, each occurrence must be treated as a separate entity.
# Example 1

# arr = [9, 9]

# output = [[],
#           [9],
#           [9],
#           [9, 9]]
# Example 2

# arr = [9, 12, 15]

# output =  [[],
#            [15],
#            [12],
#            [12, 15],
#            [9],
#            [9, 15],
#            [9, 12],
#            [9, 12, 15]]


def subsets(arr):
    if len(arr)<1:
        return [[]]
    else:
        res = []
        res.append([arr[0]])

        remain_sets = subsets(arr[1:])
        for subset in remain_sets:
            if len(subset):
                n_set = [arr[0]] + subset
                res.append(subset)
            else:
                n_set = subset
            res.append(n_set)
        return res