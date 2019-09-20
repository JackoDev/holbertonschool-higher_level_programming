#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    i = 0
    for count, number in a_dictionary.items():
        if number >= i:
            i = number
    return list(a_dictionary.keys())[list(a_dictionary.values()).index(i)]
