# Project Euler Problem 7

# Imports
from math import sqrt
from itertools import count, islice


# Check if number is prime
def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	

# Number to check if prime
answer = 0
# Number of primes found
prime = 0

# Look for 10,001 prime numbers
while prime < 10001:
	# Add to count if number is prime
	if isPrime(answer):
		prime += 1

	# Check next number
	answer += 1

# Remove final count from loop
answer -= 1

# Output
print(answer)
