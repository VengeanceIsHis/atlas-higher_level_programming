#!/usr/bin/env python3
def uppercase(str):
    Upp = ""
    for i in str:
        if 'a' <= i <= 'z':
            Upp += chr(ord(i) - ord('a') + ord('A'))
        else:
            Upp += i
    return Upp
