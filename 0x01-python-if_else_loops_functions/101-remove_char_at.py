#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for e, d in enumerate(str):
        if e != n:
            newstr += d
            return newstr
