import copy


def permute(iplist):
    '''
    Get all possibole permutations for a list of numbers
    '''
    final_compoud_list = []

    if len(iplist) == 0:
        final_compoud_list.append([])  # send empty compund list in case if empty input [[]]
    else:
        first_el = iplist[0]
        rest = iplist[1:]
        sub_compound_list = permute(rest)  # get permutation for remaining items
        # permutation of first element and all remaining items permutations
        for permut in sub_compound_list:
            for ind in range(len(permut)+1):
                permut_copy = copy.deepcopy(permut)
                permut_copy.insert(ind, first_el)
                final_compoud_list.append(permut_copy)

    return final_compoud_list
