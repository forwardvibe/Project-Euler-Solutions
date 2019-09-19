# Project Euler Problem 4

# Output variable
answer = 0

# Start loop at first 3 digit integer
for n in range(100, 1000):
	
	# Begin second loop at first loop start to reduce redundancy
	for x in range(n, 1000):
		
		# Convert product to string so we can index
		s = str(n*x)
		
		# Check first and last half for even length of output
		if len(s) % 2 == 0:
			first = s[:int(len(s)/2)]
			second = s[int(len(s)/2):]
			
		# Check first and last half for odd length of output
		else:
			first = s[:int((len(s)-1)/2)]
			second = s[int((len(s)-1)/2+1):]
		
		# Check if first and last half 
		if first == second[::-1]:
			# Create check after passing this threshold to reduce runtime
			check = n*x
			
			# Check if product is largest palindrome
			if check > answer:
				answer = check

# Output
print(answer)
