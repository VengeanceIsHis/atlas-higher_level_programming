#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    keys_list = list(a_dictionary.keys())
    result = 0
    for i in keys_list:
        if keys_list[i] == key:
            result = 1
            keys_list.remove(keys_list[i])
        if result == 1:
            keys_list.append(key)
            my_dict[key] = value
        new_dict = dict(zip(keys_list, a_dictionary.values()))
        return new_dict
