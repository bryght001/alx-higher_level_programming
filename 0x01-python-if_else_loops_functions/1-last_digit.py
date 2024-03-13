#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number_str = str(number)
last_digit = int(number_str[-1])  # Convert back to integer

first_test = 'Last digit of ' + number_str + ' is ' + number_str[-1]
if last_digit > 5:
    print(f"{first_test} and is greater than 5")
elif last_digit == 0:
    print(f"{first_test} and is zero")
elif last_digit < 6 and last_digit != 0:
    print(f"{first_test} and is less than 6 and not zero")
