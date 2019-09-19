# Project Euler Problem 5

# Imports
from math import factorial


# Function to stop nested loop with return
def smallest20():
	# Step is 2520 to reduce runtime (read description)
	for x in range(2520, factorial(20), 2520):
		# Check if divisible by every number 1 to 20
		for y in range(1, 21):
			if x % y == 0:
				# Return first number to make it to the end of the loop
				if y == 20:
					return x
			
			# Break 1-20 loop if not divisible, move on
			else:
				break


print(smallest20())
