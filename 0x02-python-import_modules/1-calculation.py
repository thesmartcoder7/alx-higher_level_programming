#!/usr/bin/python3

cal = __import__("calculator_1")

a = 10
b = 5

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, cal.add(a, b)))
    print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    print("{} / {} = {}".format(a, b, cal.div(a, b)))
    exit()
