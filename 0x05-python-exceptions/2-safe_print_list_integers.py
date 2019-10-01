#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    a, b = 0, 0
    while a < x:
        try:
            print("{:d}".format(my_list[a]), end="")
            a = a + 1
            b = b + 1
        except (ValueError, TypeError):
            a = a + 1
            continue
    print("")
    return b
