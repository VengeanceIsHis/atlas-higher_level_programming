#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list[0] == None:
        return None
    j = my_list[0]
    for i in my_list:
        if i > j:
            j = i
    return j

if __name__ == "__main__":
    main()
