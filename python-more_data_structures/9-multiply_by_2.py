#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())
    for key in list_keys:
        new_dir[key] *= 2
    return (a_dictionary)
