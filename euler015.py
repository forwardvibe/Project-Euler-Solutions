# Project Euler Problem 15

# imports
from time import time
from math import factorial

# Measure runtime
start = time()

def pascal_triangle(n):
    return factorial(n * 2) / factorial(n)**2

print(pascal_triangle(20))

# Print runtime
print("--- %s seconds ---" %(round(time() - start, 2)))
