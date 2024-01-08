#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    for i in roman_string:
        if roman_string[i] = 'I':
            result += 1
        elif roman_string[i] = 'V':
            result += 5
        elif roman_string[i] = 'X':
            result += 10
        elif roman_string[i] = 'L':
            result += 50
        elif roman_string[i] = 'C':
            result += 100
        elif roman_string[i] = 'D':
            result += 500
        elif roman_string[i] = 'M':
            result += 1000
        else:
            continue
    return result
