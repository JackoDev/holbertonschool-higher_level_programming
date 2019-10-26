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

    @staticmethod
    def from_json_string(json_string):
        """ returns json reresentation """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ for create a new instance """
        if cls.__name__ == 'Rectangle':
            insta_n = cls(1, 1)
            insta_n.update(**dictionary)
        if cls.__name__ == 'Square':
            insta_n = cls(1)
            insta_n.update(**dictionary)

        return insta_n

    @classmethod
    def load_from_file(cls):
        """ for return the class instances """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as a_file:
                reader = a_file.read()
                new1 = cls.from_json_string(reader)
                list_n = []
                for a in new1:
                    list_n.append(cls.create(**a))
        except FileNotFoundError as e:
            return []
        return list_n
