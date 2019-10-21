#!/usr/bin/python3
"""
A rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """An rectangle class"""
    def __init__(self, width, height):
        """instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width__ = width
        self.__height__ = height

    def area(self):
        """returns area of the rectangle instances"""
        return self.__width__ * self.__height__

    def __str__(self):
        """print rectangle representation"""
        return "[Rectangle] {}/{}".format(self.__width__, self.__height_)
