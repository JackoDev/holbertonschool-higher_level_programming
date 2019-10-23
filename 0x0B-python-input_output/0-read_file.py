#!/usr/bin/python3
"""module for open a file and print it in the stdout"""


def read_file(filename=""):
    """for read and write a file"""
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
