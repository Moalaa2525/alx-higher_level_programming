#!/usr/bin/python3
if_name_== "_main_":
import sys
from calculator_1 import add, sub, mul, div
if len(sys.argv) != 4:
print("Usage: ./100-my_calculator.py <a> <operator> <b>")
exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
oper = sys.argv[2]
if oper == "/":
print("{} / {} = {}".format(a, b, div(a, b)))
elif oper == "*":
print("{} * {} = {}".format(a, b, mul(a, b)))
elif oper == "-":
print("{} - {} = {}".format(a, b, sub(a, b)))
elif oper == "+":
print("{} + {} = {}".format(a, b, add(a, b)))
else:
print("Unknown operator, available operators are : +, -, /, *")
exit(1)
