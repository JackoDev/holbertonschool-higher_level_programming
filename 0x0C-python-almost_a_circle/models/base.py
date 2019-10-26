#!/usr/bin/python3
"""
Base model
"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method to return json string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ for writes JSON string representation of list """
        with open('{}.json'.format(cls.__name__), 'w') as a_file:
            if list_objs is None:
                a_file.write(cls.to_json_string([]))
            else:
                list1 = []
                for a in list_objs:
                    a = a.to_dictionary()
                    list1.append(a)
                a_file.write(cls.to_json_string(list1))
