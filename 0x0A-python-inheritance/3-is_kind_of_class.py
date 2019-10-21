#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited
from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Function to validate if a object is exactly an instance of the class
    or the parent class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
