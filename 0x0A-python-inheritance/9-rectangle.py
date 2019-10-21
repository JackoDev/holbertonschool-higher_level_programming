#!/usr/bin/python3
"""
A rectangle class
"""


BaseGeometry = __import__("8-rectangle").BaseGeometry


class Rectangle(BaseGeometry):
    """An rectangle class"""
    def __init__(self, width, height):
        """instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of the rectangle instances"""
        return self.__width * self.__height

    def __str__(self):
        """print rectangle representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
