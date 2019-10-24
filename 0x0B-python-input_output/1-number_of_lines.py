#!/usr/bin/python3
"""a new moduke to count the number of lines of a file"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file:"""
    num_line = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            num_line += 1
    return num_line

