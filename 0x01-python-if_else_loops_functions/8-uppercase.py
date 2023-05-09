#!/usr/bin/python3

def uppercase(str):
    temp = []
    for char in str:
        try:
            if not isinstance(char, str):
                temp.append(char)
        except ValueError:
            if char == char.lower() and char != " ":
                temp.append(chr(ord(char) - 32))
            else:
                temp.append(char)

    print("{}".format(''.join(temp)))
