#!/usr/bin/python3


def delete_at(arr, idx):
    if idx >= len(arr) or idx < 0:
        return arr
    else:
        del (arr[idx])
        return arr
