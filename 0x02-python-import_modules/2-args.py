#!/usr/bin/python3
if_name_ == "_name_";
import sys
tot = len(sys.argv) -1
if tot ==0 :
print("0 arguments")
elif tot == 1:
print("1 arguments")
else:
print("{} arguments".format(tot))   
for c in range(tot):
print("{}: {}".format(c + 1, sys.argv[c + 1]))
