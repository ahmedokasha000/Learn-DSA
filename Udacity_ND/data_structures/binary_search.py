# binary search with recrusion
def binary_search(arr, target):
    if len(arr) == 0:
        return False
    mid_index = len(arr)//2
    if target == arr[mid_index]:
        return True
    elif target > arr[mid_index]:
        return binary_search(arr[mid_index+1:],target)
    else:
        return binary_search(arr[:mid_index],target)



def main():
    ll = [i for i in range(50)]
    print(binary_search(ll, 5))
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
        