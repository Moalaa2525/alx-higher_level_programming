#!/usr/bin/python3
def magic_Calculatiom(a, b):
from magic-calculation_102 import add, sub
if a < b:
d = add(a, b)
for t in range(6, 8):
d = add(d, t)
return d
else:
return sub(a, b)
return 0
