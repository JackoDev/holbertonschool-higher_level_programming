#!/usr/bin/python3
"""
add_integer function to add two integers
a would be integer or no infinite float
b would be integer or no infinite float
"""


def add_integer(a, b=98):
    """
    function to add two integers
    """
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
