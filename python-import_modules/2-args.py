#!/usr/bin/python3
import sys

for arg in sys.argv:
    count = 0
    count += 1
if arg == 0:
    print("0 arguments.")
elif arg < 2:
    print("1 argument:")
    print("1: {}".format(arg))
else:
    print("{} arguments:".format(count))
    for arg in sys.argv:
        i = 1
        if arg > 0:
            print("{}: {}".format(i, arg))
