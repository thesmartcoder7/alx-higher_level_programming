#!/usr/bin/python3

for i in range(99):
    print("0{}, ".format(i) if len(str(i)) == 1 else f"{i}, ", end='')

print("{}".format(str(99)))
