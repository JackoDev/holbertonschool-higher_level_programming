#!/usr/bin/python3
"""module for task 3"""


def read_lines(filename="", nb_lines=0):
    total_lines = number_of_lines(filename)
    with open(filename, encoding='utf-8') as a_file:
        if nb_lines <= 0 or nb_lines >= total_lines:
            print(a_file.read(), end="")
        else:
            for lines in range(nb_lines):
                print(a_file.readline(), end="")


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file:"""
    num_line = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            num_line += 1
    return num_line
