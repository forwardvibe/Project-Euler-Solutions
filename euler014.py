# Project Euler Problem 14

# imports
from time import time

# Measure runtime
start = time()

# Collatz
def collatz(n):
    steps = 1
    hold = n

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        
        steps += 1

    return steps, hold

# Solution
print(max(collatz(n) for n in range(1, 10**6)))

# Print runtime
print("--- %s seconds ---" %(round(time() - start, 2)))
