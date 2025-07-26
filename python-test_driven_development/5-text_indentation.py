#!/usr/bin/python3
"""
Module for printing text with specific indentation.

This module defines the text_indentation function, which prints text with two
new lines after each '.', '?', or ':' character.
"""

def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?' or ':'.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    beg = 0
    for idx, val in enumerate(text):
        if val in '?:.':
            print(text[beg:idx + 1].strip() + '\n')
            beg = idx + 1
    if not beg:
        print(text, end='')
    elif beg != len(text):
        print(text[beg:idx + 1].strip(), end='')

