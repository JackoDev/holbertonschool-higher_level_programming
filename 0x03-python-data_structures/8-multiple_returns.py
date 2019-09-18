#!/usr/bin/python3
def multiple_returns(sentence):
    f_char = sentence[0]
    if sentence == "None" or sentence == "":
        f_char == "None"
    tuple_res = (len(sentence), f_char)
    return tuple_res
