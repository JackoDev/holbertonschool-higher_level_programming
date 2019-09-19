#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    new = list(set(my_list))
    for i in new:
        add = add + i
    return add
