#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    length = max(len(set_1),len(set_2))
    for i in length:
        if set_1[i] == set_2[i]:
            my_list.append(set_1[i])
    return my_list
