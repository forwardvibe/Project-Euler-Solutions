# Project Euler Problem 16

# imports
from time import time

# Measure runtime
start = time()

# Variables
num = 2**1000
str_num = list(str(num))
total = 0

# Solution
for i in str_num:
    total += int(i)

# Output
print(total)

# Print runtime
print("--- %s seconds ---" %(round(time() - start, 2)))
