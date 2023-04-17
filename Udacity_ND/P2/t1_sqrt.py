

def sqrt(value):
    return find_sqrt(value, 1, value - 1)

def find_sqrt(value, start, end):
    """
    Find the square root of a number using binary search recursively.
    """
    if value <= 1:
        return value

    if start == end:
        return start

    mid = (start + end) // 2
    if value // mid == mid:
        return mid
    elif value // mid < mid:
        return find_sqrt(value, start, mid - 1)
    else:
        if (mid + 1)**2 > value:
            return mid
        return find_sqrt(value, mid + 1, end)


def test_cases_sqrt():
    assert sqrt(0) == 0, f"results are unordered, results = {sqrt(0)}"
    assert sqrt(1) == 1, f"results are unordered, results = {sqrt(1)}"
    assert sqrt(2) == 1, f"results are unordered, results = {sqrt(2)}"
    assert sqrt(3) == 1, f"results are unordered, results = {sqrt(3)}"
    assert sqrt(4) == 2, f"results are unordered, results = {sqrt(4)}"
    assert sqrt(5) == 2, f"results are unordered, results = {sqrt(5)}"
    assert sqrt(6) == 2, f"results are unordered, results = {sqrt(6)}"
    assert sqrt(7) == 2, f"results are unordered, results = {sqrt(7)}"
    assert sqrt(8) == 2, f"results are unordered, results = {sqrt(8)}"
    assert sqrt(9) == 3, f"results are unordered, results = {sqrt(9)}"
    assert sqrt(10) == 3, f"results are unordered, results = {sqrt(10)}"
    assert sqrt(11) == 3, f"results are unordered, results = {sqrt(11)}"
    assert sqrt(12) == 3, f"results are unordered, results = {sqrt(12)}"
    assert sqrt(13) == 3, f"results are unordered, results = {sqrt(13)}"
    assert sqrt(14) == 3, f"results are unordered, results = {sqrt(14)}"
    assert sqrt(15) == 3, f"results are unordered, results = {sqrt(15)}"
    assert sqrt(16) == 4, f"results are unordered, results = {sqrt(16)}"
    assert sqrt(17) == 4, f"results are unordered, results = {sqrt(17)}"
    assert sqrt(18) == 4, f"results are unordered, results = {sqrt(18)}"
    assert sqrt(19) == 4, f"results are unordered, results = {sqrt(19)}"
    assert sqrt(20) == 4, f"results are unordered, results = {sqrt(20)}"

    
    
def main():
    # test_cases_sqrt()
    test_cases_sqrt2()
if __name__ == '__main__':
    main()