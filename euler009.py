# Project Euler Problem 9

for a in range(1, 1000):
	for b in range(a, 1000):
		c = (a**2 + b**2)**0.5
		
		if a + b + c == 1000:
      # Output
			print(int(a * b * c))
