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
