#!/usr/bin/python3

for i in range(99):
    print(f"0{i}, " if len(str(i)) == 1 else f"{i}, ", end='')

print(str(99))
