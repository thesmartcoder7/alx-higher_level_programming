#!usr/bin/python3


def safe_print_list(arr, items):
    """
        Print certain elements of a list
    """
    j = 0

    try:
        for i in arr:
            if j < items:
                print('{}'.format(arr[j]), end='')
                j += 1

        print()
    except TypeError:
        pass
    finally:
        return j
