#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print("Last digit of ", end='')
if number >= 0 and last_digit > 5:
    print(f"{number} is {last_digit} and is greater than 5")
elif number >= 0 and last_digit == 0:
    print(f"{number} is {last_digit} and is 0")
elif number >= 0 and last_digit < 6 and last_digit != 0:
    print(f"{number} is {last_digit} and is less than 6 and not 0")
elif number < 0 and -abs(last_digit) > 5:
    last_digit = -abs(last_digit)
    print(f"{number} is {last_digit} and is greater than 5")
elif number < 0 and -abs(last_digit) == 0:
    last_digit = -abs(last_digit)
    print(f"{number} is {last_digit} and is 0")
else:
    last_digit = -abs(last_digit)
    print(f"{number} is {last_digit} and is less than 6 and not 0") 
