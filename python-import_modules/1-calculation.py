#!/usr/bin/python3
import calculator_1 as cal
def main()
    a = 10
    b = 5
    addres = cal.add(a, b) 
    subres = cal.sub(a, b)
    mulres = cal.sub(a, b)
    divres = cal.sub(a, b)
    print("{} + {} = {}".format(a, b, addres))
    print("{} - {} = {}".format(a, b, subres))
    print("{} * {} = {}".format(a, b, mulres))
    print("{} / {} = {}".format(a, b, divres))


if __name__ == "__main__":
    main()
