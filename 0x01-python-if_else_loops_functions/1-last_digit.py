#!/usr/bin/python3
import random

i = random.randint(-10000, 10000)

ld = int(str(i)[-1])

if ld > 5 and i > 0:
    print(f"Last digit of {i} is {ld} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {i} is {ld} and is 0")
elif i < 0:
    print(f"Last digit of {i} is -{ld} and is less than 6 and not 0")
else:
    print(f"Last digit of {i} is {ld} and is less than 6 and not 0")
