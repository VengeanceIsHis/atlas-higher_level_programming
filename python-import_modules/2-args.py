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
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(count))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
