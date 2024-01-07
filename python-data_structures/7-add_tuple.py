#!/usr/bin/python3                                                              
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 2:
       len1 = 2
    elif len(tuple_b) > 2:
        len2 = 2
    else:
       len1 = len(tuple_a)
       len2 = len(tuple_b)
    if len2 > len1:
        truelen = len2
    else:
        truelen = len1
    i = 0
    tuple1 = tuple_a[i] + tuple_b[i]
    tuple2 = tuple_a[i + 1] + tuple_b[i + 1]
    result_tuple = (tuple1, tuple2)
    return result_tuple
if __name__ == "__main__":
    main()


