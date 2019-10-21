#!/usr/bin/python3
"""
    prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """new class MyList that inherits from list"""
    def print_sorted(self):
        """print a list in ascending sort"""
        print(sorted(self))
