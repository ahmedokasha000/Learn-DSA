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


def main():
    path = "/meda/ahmed000/Personal/Learning/Learn-DSA"
    print(f"{isdir(path)} , {isdir(path)}")
    res = find_files('.pyc',path)
    print('\n'.join(res))
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass