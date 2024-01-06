#!/usr/bin/python3
import sys
def main():
    count = -1
    for arg in sys.argv:
        count += 1
    if count == 0:
        print("0 arguments.")
    elif count < 2:
        print("1 argument:")
        print("1: {}".format(arg))
    else:
        print("{} arguments:".format(count))
        2count = -1
        for arg in sys.argv:
            2count += 1
            i = 1
            if 2count > 0:
                print("{}: {}".format(i, arg))
if __name__ == "__main__":
    main()
