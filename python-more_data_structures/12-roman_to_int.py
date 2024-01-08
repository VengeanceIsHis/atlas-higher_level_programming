#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    prev_value = 0
    current_value = 0
    for char in roman_string:
        if char == 'I':
            current_value += 1
        elif char == 'V':
            current_value += 5
        elif char == 'X':
            current_value += 10
        elif char == 'L':
            current_value += 50
        elif char == 'C':
            current_value += 100
        elif char == 'D':
            current_value += 500
        elif char == 'M':
            current_value += 1000
        else:
            continue
        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value
            prev_value = current_value
        return result
