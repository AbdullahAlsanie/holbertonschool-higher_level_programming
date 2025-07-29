#!/usr/bin/python3
"""
This module contains a Class square
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

    def size(self):
        """ retrieve the size"""
        return (self.__size)

    def size(self, value):
        """ set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ this method returns a the area of the square"""

        return (self.__size ** 2)
