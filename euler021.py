# Project Euler Problem 21

# imports
from time import time
from math import sqrt

# Measure runtime
start = time()

# Solution
def d(n):
    return 1 + sum([n / i + i for i in range(2, int(sqrt(n))) if n % i == 0])

total = 0
a = 2

while a < 10000:
    if d(d(a)) == a and d(a) != a:
        total += a

    a += 1

print(total)

# Print runtime
print("--- %.2f seconds ---" %(time() - start))
