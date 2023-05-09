#!/usr/bin/python3

def islower(c):
    try:
        if abs(int(c)):
            return False
    except ValueError:
        return True if c == c.lower() else False
