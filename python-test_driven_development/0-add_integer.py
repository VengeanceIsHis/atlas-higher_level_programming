#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, float):
       int_a = int(a)
    if isinstance(b, float):
        int_b = int(b)
    else:
        int_a = a
        int_b = b
    if not isinstance(int_a, int):
        raise TypeError("a must be an integer")
    if not isinstance(int_b, int):
        raise TypeError("b must be an integer")
    return int_a + int_b