# binary search with recrusion
def binary_search_contains(arr, target):
    if len(arr) == 0:
        return False
    mid_index = len(arr) // 2
    if target == arr[mid_index]:
        return True
    elif target > arr[mid_index]:
        return binary_search_contains(arr[mid_index+1:],target)
    else:
        return binary_search_contains(arr[:mid_index],target)

def binary_search_recursive(array, target):
    '''
    This function will call `binary_search_recursive_soln` function.
    You don't need to change this function.
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    if end_index <= start_index:
        return -1
    mid_index = start_index + (end_index - start_index) // 2
    if target == array[mid_index]:
        return mid_index
    elif target > array[mid_index]:
        start_ind = mid_index +1
        return binary_search_recursive_soln(array, target, start_ind, end_index)
    else:
        end_index = mid_index
        return binary_search_recursive_soln(array, target, start_ind, end_index)


def main():
    ll = [1]
    print(binary_search(ll, 5))
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
        