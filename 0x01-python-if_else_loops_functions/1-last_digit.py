#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
d = d * -1 if number < 0 else d

if d > 5:
    print(f"Last digit of {number} is {d} and is greater than 5")
elif d == 0:
    print(f"Last digit of {number} is {d} and is 0")
elif d < 6 and d != 0:
    print(f"Last digit of {number} is {d} and is less than 6 and not 0")
