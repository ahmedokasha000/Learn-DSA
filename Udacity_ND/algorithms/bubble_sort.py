from random import shuffle
import time








def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.2f}")
        return result
    return wrapper


@timeit
def bubble_sort(data: list):
    """
    Sorts a list of integers using inplace bubble sort algorithm.

    :param data: The list of integers to be sorted.
    :type data: list
    :return: None
    """
    last_ind = len(data) - 1
    for ind in range(len(data) - 1):
        for ind in range(last_ind):
            if data[ind + 1] < data[ind]:
                data[ind], data[ind + 1] = data[ind + 1], data[ind]
        last_ind -= 1


def main():
    test_sample = list(range(1000))
    shuffle(test_sample)

    bubble_sort(test_sample)
    # print(test_sample)
    # assert bubble_sort(test_sample) == list(range(10)), "results are unordered"

    test_sample = []
    bubble_sort(test_sample)
    assert test_sample == [], f"results are unordered, sample = {[]}, results = {test_sample}"
    print(test_sample)


if __name__ == '__main__':
    main()