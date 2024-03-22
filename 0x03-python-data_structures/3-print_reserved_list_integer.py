#!/usr/bin/python3
def print_reserved_list_integer(my_list=[]):
if not my_list:
return None
for t in reversed(my_list):
print("{:d}".format(t))
