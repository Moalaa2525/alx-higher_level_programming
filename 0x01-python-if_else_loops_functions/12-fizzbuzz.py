#!/usr/bin/python3
def fizzbuzz():
    for c in range (1, 101):
        if c % 10 == 0:
            print("FizzBuzz", end= "")
        elif c % 5 == 0:
            print("Buzz", end="")
        elif c % 3 == 0:
            print("Fizz", end="")
        else:
            print("{:d}".format(c), end="")
    
