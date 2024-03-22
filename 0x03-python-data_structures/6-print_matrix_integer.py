#!/usr/bin/python3
def print_matrix_integer(matri=[[]]):
if not matrix:
return None
for submatrix in matrix:
if len(submatrix)  == 0:
print()
for t in range(len(submatrix)):
print("{:d}".format(submatrix[t]), end="\n" if t is len(submatrix) -1 else " ")
