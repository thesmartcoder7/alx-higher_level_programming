#!/usr/bin/python3

def uppercase(str):
    temp = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            temp += chr(ord(str[i]) - 32)
            continue
        temp += str[i]

    # print('{}'.format(temp))
    return '{}'.format(temp)
