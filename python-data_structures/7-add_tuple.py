#!/usr/bin/python3                                                              
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 > 2:
        len1 = 2
    if len2 > 2:
        len2 = 2
    if len1 == 1:
        tuple_a[1] = 0
    elif len1 == 0:
        tuple_a[0] = 0
    if len2 == 1:
        tuple_b[1] = 0
    elif len2 == 0:
        tuple_b[0] = 0
    tuple1 = tuple_a[0] + tuple_b[0]
    tuple2 = tuple_a[1] + tuple_b[1]
    result_tuple = (tuple1, tuple2)
    return result_tuple
if __name__ == "__main__":
    main()


