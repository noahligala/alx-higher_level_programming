#!/usr/bin/python3

def element_at(my_list, idx):
    # check if idx is negative or out of range #
    if idx < 0 or idx >= len(my_list):
        return None

    # return the element at ehe specified index #
    return my_list[idx]
