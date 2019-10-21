#!/usr/bin/python3
"""
A base class BaseGeometry
"""


class BaseGeometry():
    """An empty class"""
    pass

    def area(self):
        """for raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """for validate the value"""
        if type(value) is not int:
            raise Exception("{} must be an integer".format(name))
        if value <= 0:
            raise Exception("{} must be greater than 0".format(name))
