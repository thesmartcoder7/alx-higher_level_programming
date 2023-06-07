#!/usr/bin/python3
"""
    This module prints a text with a 2 new lines after each of
    these characters: `.`, `?`, `:`
"""


def text_indentation(text):
    """
        Prints a text with indentation

        Arguments:
            text (str): The text to prints.
        Raises:
            TypeError: If `text` isn't string.
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    txt_len = len(text)
    idx = 0
    new_str = ''
    start = True

    while idx < txt_len:
        if text[idx] == ' ' and start is True:
            idx += 1
            continue

        start = False

        if text[idx] in '.?:':
            new_str += text[idx]
            new_str += '\n'
            new_str += '\n'
            idx += 1

            while idx < txt_len and text[idx] == ' ':
                idx += 1

            continue

        if idx < txt_len:
            new_str += text[idx]
            idx += 1

    print(new_str, end='')
