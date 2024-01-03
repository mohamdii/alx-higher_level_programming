#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "and is greater than 5 and not 0"
str2 = "is 0"
str3 = "and is less than 6 and not 0"
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit < 5:
    print(f"Last digit of {number} is {lastdigit} {str3}")
elif lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} {str2}")
elif lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} {str3}")

