#!/usr/bin/python3
# sys module gives access to the arguments
import sys
from calculator_1 import add, sub, mul, div

# sys.argv gives an array or agruments including
# the name of the script. [1:] removes the name
# of the script from the list

args = sys.argv[1:]
ops = {'+': add, '-': sub, '*': mul, '/': div}

if __name__ == "__main__":
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if args[1] not in ops:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(args[0])
            b = int(args[2])
            op = args[1]
            print(f"{a} {op} {b} = {ops[op](a, b)}")
            exit()
