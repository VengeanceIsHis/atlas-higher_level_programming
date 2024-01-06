#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def main():
    a = 10
    b = 5
    addres = add(a, b) 
    subres = sub(a, b)
    mulres = mul(a, b)
    divres = div(a, b)
    print("{} + {} = {}".format(a, b, addres))
    print("{} - {} = {}".format(a, b, subres))
    print("{} * {} = {}".format(a, b, mulres))
    print("{} / {} = {}".format(a, b, divres))


if __name__ == "__main__":
    main()
