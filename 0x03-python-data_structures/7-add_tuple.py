#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    fst_tuple = tuple_a + (0, 0)
    scd_tuple = tuple_b + (0, 0)
    fst_tuple = fst_tuple[0:2]
    scd_tuple = scd_tuple[0:2]
    result = (fst_tuple[0] + scd_tuple[0], fst_tuple[1] + scd_tuple[1])
    return result
