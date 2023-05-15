#!/usr/bin/python3


def delete_at(arr, idx):
    if idx >= len(arr) or idx < 0:
        return arr
    else:
        new = []
        for i in range(len(arr)):
            if i == idx:
                continue
            else:
                new.append(arr[i])
        return new
