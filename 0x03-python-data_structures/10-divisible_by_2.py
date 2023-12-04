#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # create a new list with True or False
    # depending on whether the integer is a multiple of 2
    result_list = [num % 2 == 0 for num in my_list]
    return result_list
