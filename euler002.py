# Project Euler Problem 2

# Running total
total = 0

# List to generate fibonacci sequence
fibonacci = [1, 2]

# Check until numbers reach over 4,000,000
while fibonacci[1] < 4000000:
	
	# Sequence through fibonacci numbers
	temp = fibonacci[1]
	fibonacci[1] += fibonacci[0]
	fibonacci[0] = temp
	
	# Add to total if number is even
	if fibonacci[0] % 2 == 0:
		total += fibonacci[0]
	
# Output
print(total)
