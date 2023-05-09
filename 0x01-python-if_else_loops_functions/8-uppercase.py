#!/usr/bin/python3

def uppercase(str):
    temp = []
    for char in str:
        try:
            if isinstance(int(char), int):
                temp.append(char)
        except TypeError:
            if char == char.lower() and char != " ":
                temp.append(chr(ord(char) - 32))
            else:
                temp.append(char)

    print(''.join(temp))
