from random import shuffle


def quick_sort(data: list):
    """_summary_

    Args:
        data (list): _description_
        start (int): _description_
        end (int): _description_
    """
    if len(data) <= 1:
        return data

    smaller_array, greater_array = [], []

    pivot = data[-1]
    for element in data[:-1]:
        if element <= pivot:
            smaller_array.append(element)
        else:
            greater_array.append(element)

    return quick_sort(smaller_array) + [pivot] + quick_sort(greater_array)


def main():
    test_sample = list(range(10000))
    shuffle(test_sample)


    assert quick_sort(test_sample) == list(range(10000)), "results are unordered"

    test_sample = []
    assert quick_sort(test_sample) == [], f"results are unordered, sample = {[]}, results = {test_sample}"


if __name__ == '__main__':
    main()