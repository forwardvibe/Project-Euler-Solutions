# Project Euler Problem 35

# Imports
from math import sqrt
from itertools import count, islice


# Check if number is prime
def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

	
# Variable to store all sets of rotational primes
primes = []

# Loop through numbers up to 1,000,000
for n in range(1000001):
	
	# Check if number is prime
	if isPrime(n):
		
		# If number is prime, break digits into list items
		x = list(str(n))
		
		# List to store a single set of rotational primes in
		prime_set = []
		
		# For each digit in a prime number
		for i, y in enumerate(x):
			
			# Move the first digit to the end
			temp = x[0]
			x.pop(0)
			x.append(temp)
			
			# If new rotation is also prime, append to list
			if isPrime(int(''.join(x))):
				prime_set.append(int(''.join(x)))
			
			# If not prime, move on to next number (halves run time)
			else:
				break
			
		# If all rotations are prime, add group to final list 
		if len(prime_set) == len(x):
			primes.append(int(''.join(x)))
			
			# Output
			print('%i\t' %(len(primes)), prime_set)
