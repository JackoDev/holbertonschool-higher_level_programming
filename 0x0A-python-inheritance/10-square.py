#!/usr/bin/python3
"""
square class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class for square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return .__size ** 2
