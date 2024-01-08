#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    for char in roman_string:
        if roman_string[char] = 'I':
            result += 1
        elif roman_string[char] = 'V':
            result += 5
        elif roman_string[char] = 'X':
            result += 10
        elif roman_string[char] = 'L':
            result += 50
        elif roman_string[char] = 'C':
            result += 100
        elif roman_string[char] = 'D':
            result += 500
        elif roman_string[char] = 'M':
            result += 1000
        else:
            continue
    return result
