#!/usr/bin/python3
for c in range(10):
    for e in range(c, 10):
        if c < e:
            print ("{:d} {:d}".format(c, e)),
            end ="\n" if c == 8 and e == 9 else ", "
