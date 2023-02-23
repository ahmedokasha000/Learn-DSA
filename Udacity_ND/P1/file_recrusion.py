from os import listdir
# from os import path
from os.path import isfile, isdir, join, expanduser


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    valid_paths = []
    if isfile(path):
        if path.endswith(suffix):
            valid_paths.append(path)
    elif isdir(path):
        child_dirs = listdir(path)
        for childp in child_dirs:
            valid_paths.extend(find_files(suffix, join(path, childp)))

    return valid_paths


def test_cases():

    path = "/media/ahmed000/Personal/Learning/Learn-DSA/Udacity_ND/P1/testdir"

    # Test Case 1
    res = find_files('.c', path)
    assert len(res) == 4
    print("Test Case 1 passed.")

    # Test Case 2
    res = find_files('.c', path)
    valid_path = False
    for file_path in res:
        if file_path.endswith("testdir/subdir3/subsubdir1/b.c"):
            valid_path = True
            break
    assert valid_path
    print("Test Case 2 passed.")

    # Test Case 3
    res = find_files('.py', path)
    assert len(res) == 0
    print("Test Case 3 passed.")


def main():
    test_cases()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
