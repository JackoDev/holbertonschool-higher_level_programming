#!/usr/bin/python3
"""
task 2
"""


from models.base import Base


class Rectangle(Base):
    """New class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """print to stdout the rectangle"""
        for line in range(self.y):
            print()
        for a in range(self.height):
            for blank in range(self.x):
                print(" ", end="")
            for b in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args):
        for number in range(len(args)):
            if number == 0:
                self.id = args[0]
            elif number == 1:
                self.width = args[1]
            elif number == 2:
                self.height = args[2]
            elif number == 3:
                self.x = args[3]
            elif number == 4:
                self.y = args[4]
