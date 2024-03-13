#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number_str = str(number)

def get_last_digit(number):
 #"""Extracts the last digit (as an integer, handling negative numbers)."""
    if number >= 0:
        return number % 10
    else:
        return (abs(number) % 10) * -1  # Handle negative case
        
        
last_digit = get_last_digit(number)
last_digit_str = str(last_digit)

first_test = 'Last digit of ' + number_str + ' is ' + last_digit_str
if last_digit > 5:
    print(f"{first_test} and is greater than 5")
elif last_digit == 0:
    print(f"{first_test} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"{first_test} and is less than 6 and not zero")
