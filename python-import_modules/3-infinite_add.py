#!/usr/bin/python3
import sys


def main():
    result = 0;
    for arg in sys.argv:
        result += arg
    print(f"{result}")

    
if __name__ == "__main__":
    main()
