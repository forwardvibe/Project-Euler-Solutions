# Project Euler Problem 12

# imports
from time import time
from math import sqrt

# Measure runtime
start = time()

# Variables
total = 0
triangle = 1
increment = 2

# Find divisors
while True:
    triangle += increment
    limit = int(sqrt(triangle))

    for i in range(2, limit):
        if triangle % i == 0:
            total += 2

    if total >= 500:
        print(triangle)
        break
            
    limit = 0
    increment += 1
    total = 0

# Output runtime
print("--- %s seconds ---" % (round(time() - start, 2)))
