# Project Euler Problem 1

# Running total
total = 0

# Loop up to 1000
for n in range(1000):
	
	# Add number to total if divisible by 3 or 5
	if n % 3 == 0 or n % 5 == 0:
		total += n

# Output
print(total)
