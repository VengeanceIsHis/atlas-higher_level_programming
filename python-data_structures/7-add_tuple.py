#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    len1, len2 = (2, len2) if len1 > 2 else (len1, len2)
    tuple_a = (*tuple_a, 0, 0)[:2]
    tuple_b = (*tuple_b, 0, 0)[:2]

    tuple1 = tuple_a[0] + tuple_b[0]
    tuple2 = tuple_a[1] + tuple_b[1]
    result_tuple = (tuple1, tuple2)
    return result_tuple


if __name__ == "__main__":
    main()
