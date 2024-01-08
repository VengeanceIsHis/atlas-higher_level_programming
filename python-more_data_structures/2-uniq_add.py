#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    unique = set(new_list)
    return sum(unique)
