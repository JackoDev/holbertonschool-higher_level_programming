#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    a, b = 0, 0
    while a < x:
        try:
            print("{}".format(my_list[a]), end="")
            b = b + 1
            a = a + 1
        except IndexError:
            a = a + 1
    print("")
    return b
