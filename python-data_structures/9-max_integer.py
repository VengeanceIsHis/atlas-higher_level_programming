#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list[0]:
        return None
    j = my_list[0]
    for i in my_list:
        if i > j:
            j = i
    return j

if __name__ == "__main__":
    main()
