#!/usr/bin/python3 

def remove_char_at(srt, n):
    new_str = []
    for i in range(len(srt)):
        if i != n:
            new_str.append(srt[i])
    return ''.join(new_str)
