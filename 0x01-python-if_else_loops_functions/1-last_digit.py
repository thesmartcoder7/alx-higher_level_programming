#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)

if n < 0:
    d = n % (-10)
else:
    d = n % 10

if d > 5:
    print("Last d of {} is {} and is greater than 5".format(n, d))
elif d == 0:
    print("Last d of {} is {} and is 0".format(n, d))
else:
    print("Last d of {} is {} and is less than 6 and not 0".format(n, d))
