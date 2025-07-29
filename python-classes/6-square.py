#!/usr/bin/python3
"""
This module contains a Class square
"""


class Square:
    """
    This Class represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ retrieve the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve position"""
        return (self.__position)

    @postition.setter
    def position(self, position):
        """set position"""
        self.__validate_position(position)
        self.__position = position
        return (self.position)

    def area(self):
        """ this method returns a the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """
        prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """

        if self.size == 0:
            print()
            return
        print(
            "\n" * self.__position[1]
            + ((" " * self.__position[0] + "#" * self.__size) + "\n")
            * self.__size,
            end="",
            )

    def __validate_position(self, position):
        """ validate the position"""
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
