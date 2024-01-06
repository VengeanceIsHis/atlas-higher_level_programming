#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
            two_digit_number = f"{i:02d}{j:02d}"
            print(two_digit_number)
