#!/usr/bin/python3

for i in range(122, 96, -1):
    letter = chr(i)
    l_case = chr(i - 32) if i % 2 != 0 else letter
    print("{}".format(l_case), end="")
