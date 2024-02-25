#!/usr/bin/python3
import random
import math
number = random.randint(-10, 10)
Nod = number % 10 if number > 10 else number % -10
print(
    "Last digit of {:d} is {:d} and is "
    .format(number, Nod), end="")
if Nod > 5:
    print("This is greater than 5")
    
elif Nod == 0:
    print("0")
else:
    print("This would be less than 6 ")
