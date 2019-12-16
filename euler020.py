# Project Euler Problem 20

# imports
from time import time
from math import factorial

# Measure runtime
start = time()

# Solution
print(sum([int(x) for x in list(str(factorial(100)))]))

# Print runtime
print("--- %s seconds ---" %(round(time() - start, 2)))
