#!/usr/bin/python3


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    count = 0
    new = ""
    for i in text:
        if count == 1:
            new = ""
            count = 0
        if i not in "?:.":
            new += i
        else:
            new += i
            print(new.strip())
            print()
            count = 1
    if count == 0 and '\n' not in new:
        print(new.strip(), end="")
    elif count == 0:
        print(new.strip())
