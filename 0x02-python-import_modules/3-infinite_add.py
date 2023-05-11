#!/usr/bin/python3

# sys module gives access to the arguments
import sys

# sys.argv gives an array or agruments including
# the name of the script. [1:] removes the name
# of the script from the list
args = sys.argv[1:]
total = 0

if __name__ == "__main__":
    for arg in args:
        total += int(arg)

    print(total)
    exit()
