#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i, j in enumerate(new):
        if j == search:
            new[i] = replace
    return new
