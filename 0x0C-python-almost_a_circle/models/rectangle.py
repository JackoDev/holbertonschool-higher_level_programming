#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """ New class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the private attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the attribute for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the attribute for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get the private attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the attribute value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get the private attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the attribute value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of the rectangle """
        return (self.width * self.height)

    def display(self):
        """ print to stdout the rectangle """
        for line in range(self.y):
            print()
        for a in range(self.height):
            for blank in range(self.x):
                print(" ", end="")
            for b in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ return a string """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ for update the args given to the class """
        if args:
            for number in range(0, len(args)):
                if number == 0:
                    self.id = args[number]
                elif number == 1:
                    self.width = args[number]
                elif number == 2:
                    self.height = args[number]
                elif number == 3:
                    self.x = args[number]
                elif number == 4:
                    self.y = args[number]
        else:
            for num, value in kwargs.items():
                if num == 'width':
                    self.width = value
                elif num == 'height':
                    self.height = value
                elif num == 'x':
                    self.x = value
                elif num == 'y':
                    self.y = value
                elif num == 'id':
                    self.id = value

    def to_dictionary(self):
        """ for return attributes of the dictionary """
        names = ["id", "width", "height", "x", "y"]
        sets = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(names, sets))
