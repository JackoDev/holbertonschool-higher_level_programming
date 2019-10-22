#!/usr/bin/python3
"""
Base model
"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(sel, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
