#!/usr/bin/python3
"""
This module contains a square class
"""


class Square:
    """
    This Class represents a square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
