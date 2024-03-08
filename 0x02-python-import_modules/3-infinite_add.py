#!/usr/bin/python3
if_name_== "_main_":
import sys
total = 0
for c in range(len(sys.argv) -1):
total += int(sys.argv[c + 1])
print(total)
