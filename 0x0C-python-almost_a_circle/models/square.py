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

    def update(self, *args, **kwargs):
        """ function to update Square """
        if args:
            for num in range(0, len(args)):
                if num == 0:
                    self.id = args[num]
                elif num == 1:
                    self.size = args[num]
                elif num == 2:
                    self.x = args[num]
                elif num == 3:
                    self.y = args[num]
        else:
            for num1, value in kwargs.items():
                if num1 == 'size':
                    self.size = value
                elif num1 == 'x':
                    self.x = value
                elif num1 == 'y':
                    self.y = value
                elif num1 == 'id':
                    self.id = value
