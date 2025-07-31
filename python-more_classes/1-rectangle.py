#!/usr/bin/python3
"""
This module containe a rectangle class
"""


class Rectangle:
    """
    this class represents a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = valid_width(value)
        self.__height = valid_height(value)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = valid_width(value)

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = valid_height(value)

    def valid_width(self, value):
        """validate the width"""
        if value is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return (value)

    def valid_height(self, value):
        """ validate the height"""
        if value is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return (value)
