#!/usr/bin/python3
import sys


def main():
    result = 0
    for i, arg in enumerate(sys.argv[1:], start=1):
        result += int(sys.argv[i])
    print(f"{result}")


if __name__ == "__main__":
    main()
