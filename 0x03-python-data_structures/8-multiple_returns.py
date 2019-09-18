#!/usr/bin/python3
def multiple_returns(sentence):
    f_char = ""
    if (len(sentence) == 0):
        f_char = None
    else:
        f_char = sentence[0]
    tuple_res = (len(sentence), f_char)
    return tuple_res
