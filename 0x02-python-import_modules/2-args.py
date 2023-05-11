#!/usr/bin/python3

# sys module gives access to the arguments
import sys

# sys.argv gives an array or agruments including
# the name of the script. [1:] removes the name
# of the script from the list
args = sys.argv[1:]
total = len(args)

if __name__ == "__main__":
    if total == 0:
        print("0 arguments.")
        exit()
    else:
        print(f"{total} argument{'s' if total > 1 else ''}:")
        for i in range(total):
            print(f"{i+1}: {args[i]}")
