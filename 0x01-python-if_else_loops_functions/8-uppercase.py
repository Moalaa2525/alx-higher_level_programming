#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
    
def uppercase(str):
    for d in str:
        print("{:d}"
              .format(ord(d) if not islower else ord(d) -32),
              end= "")
        print=""
