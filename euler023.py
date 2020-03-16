# Project Euler Problem 23

# Imports
from time import time
from math import sqrt

# Measure runtime
start = time()


# Find proper divisors of a number n
def divisors(n):
	divisors = [1]
	upperLimit = int(sqrt(n))

	# Append both divisors to list
	for i in range(2, upperLimit + 1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n // i)
	
	# Only input divisor once if square root
	if upperLimit**2 == n:
		divisors.pop()

	return(divisors)

# Check if number is abundant
def abundant(n):
	return n < sum(divisors(n))


# Variables
upperLimit = 28123
abundants = []
abundantSums = set()

# Find abundant numbers under limit
for i in range(3, upperLimit):
	if abundant(i):
		abundants.append(i)

# Add every pair of abundant numbers together
for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		num = abundants[i] + abundants[j]
		
		# Add the unique sums to set
		if num < upperLimit:
			abundantSums.add(num)

# Subtract sum of abundant pairs from sum of every number up to limit
total = int((upperLimit - 1) * upperLimit / 2) - sum(abundantSums)
print(total)

# Print runtime
print("--- %.2f seconds ---" %(time() - start))
