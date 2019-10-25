#!/usr/bin/python3
""" square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class for square  """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(id=id, x=x, y=y, width=size, height=size)
        self.size = size

    @property
    def size(self):
        """ get the size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ set the attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """ return a string """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
