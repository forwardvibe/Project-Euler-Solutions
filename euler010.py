# Project Euler Problem 10

# Imports
from math import sqrt
from itertools import count, islice
import time

# Track runtime
start_time = time.time()

# Check if number is prime
def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	
	
# Set upper limit
limit = 2000000
# Running sum total
total = 0

# Add number to total if prime
for n in range(limit):
	if isPrime(n):
		total += n
		
# Output
print(total)
print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
# Runtime ~35 seconds
