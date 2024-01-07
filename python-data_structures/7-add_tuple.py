#!/usr/bin/python3                                                              
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 > 2:
        len1 = 2
    if len2 > 2:
        len2 = 2
    truelen = max(len1, len2)

    tuple1 = tuple_a[0] if len1 > 0 else 0 + tuple_b[0] if len2 > 0 else 0
    tuple2 = tuple_a[1] if len1 > 1 else 0 + tuple_b[1] if len2 > 1 else 0
    result_tuple = (tuple1, tuple2)
    return result_tuple
if __name__ == "__main__":
    main()


