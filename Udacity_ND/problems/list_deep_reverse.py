def deep_reverse(arr):
    arr.reverse()
    for item in arr:
        if isinstance(item, list):
            deep_reverse(item)
    return arr