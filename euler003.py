# Project Euler Problem 3

# Imports
from math import sqrt
from itertools import count, islice


# Check if number is prime
def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	

# Set target
target = 600851475143
largest_prime_factor = 0

# Only check up to sqrt(target) - 1 because after that everything repeats
for n in range(1, int(sqrt(target) - 1)):
	
	# Set new lpf if divisible and prime
	if target % n == 0 and isPrime(n):
		largest_prime_factor = n
		
# Output
print(largest_prime_factor)
