#!/usr/bin/python3
def safe_print_list(my_list=[], x = 0):
    try:
        for index in my_list:
        print("{}".format(index), end='')
        if index == x:
            break:
    return index
    except:
        return None
        
