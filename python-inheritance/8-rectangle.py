#!/usr/bin/python3
"""basegeometryclass"""


class BaseGeometry:

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value for integer and positive"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class rectangle"""


class Rectangle(BaseGeometry):
    """creates rectangle class"""
    def __init__(self, width, height):
        """initializes rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
