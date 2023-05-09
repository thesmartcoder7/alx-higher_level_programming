#!/usr/bin/python3

for one in range(10):
    for two in range(10):
        if int(f"{one}{two}") < int(f"{two}{one}"):
            if f"{one}{two}" != str(89):
                print(f"{one}{two}, ", end='')
            else:
                print(f"{one}{two}")
