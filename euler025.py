# Imports
from itertools import permutations
from time import time

# Measure runtime
start = time()

# Begin fibonacci sequence
fibonacci = [1, 1]

tracker = 2
while len(str(fibonacci[1])) < 1000:
	temp = fibonacci[1]
	fibonacci[1] = fibonacci[0] + fibonacci[1]
	fibonacci[0] = temp
	tracker += 1
print(tracker)

		
# Print runtime
print("--- %.2f seconds ---" %(time() - start))
