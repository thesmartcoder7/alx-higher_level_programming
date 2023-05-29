#!usr/bin/python3


def get_length(arr):
    """
        Get the length of any list
    """
    length = 0
    try:
        for item in arr:
            length += 1
        return length
    except TypeError as error:
        print(error)
        raise


def safe_print_list(arr, items):
    """
        Print certain elements of a list
    """
    length = get_length(arr)
    try:
        printed = 0
        if items > length:
            for i in range(length):
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
