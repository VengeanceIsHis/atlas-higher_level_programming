#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
while number > 0:
    last_digit = number % 10
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
        break
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
        break
    else:
        print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
        break
while number < 0:
    last_digit = abs(number) % 10
    if last_digit > 5:
        print(f"Last digit of {number} is -{last_digit} and is greater than 5")
        break
    elif last_digit == 0:
        print(f"Last digit of {number} is -{last_digit} and is 0")
        break
    else:
        print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")
        break
