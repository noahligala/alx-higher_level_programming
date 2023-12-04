#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list), 0, -1):
        if num >= 0 or num < len(my_list):
            print("{}".format(num))
