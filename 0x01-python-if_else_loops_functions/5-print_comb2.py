#!/usr/bin/python3

for integer in range(99):
    print(f"0{integer}, " if len(str(integer)) == 1 else f"{integer}, ", end='')

print(str(99))
