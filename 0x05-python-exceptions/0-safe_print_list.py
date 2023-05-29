#!usr/bin/python3


def get_length(arr):
    """
        Get the length of any list
    """
    len = 0
    try:
        for item in arr:
            len += 1
        return len
    except TypeError as error:
        print(error)
        raise


def safe_print_list(arr, items):
    """
        Print certain elements of a list
    """
    len = get_length(arr)
    try:
        printed = 0
        if items > len:
            for i in range(len):
                print(arr[i], end='')
                printed += 1
            print()
        else:
            for i in range(items):
                print(arr[i], end='')
                printed += 1
            print()
        return printed
    except IndexError as error:
        print(error)
        raise
