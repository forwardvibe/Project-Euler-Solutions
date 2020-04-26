# Imports
from itertools import permutations
from time import time

# Measure runtime
start = time()

# Identify 1,000,000th permutation
print(''.join(list(permutations('0123456789'))[999999]))
		
# Print runtime
print("--- %.2f seconds ---" %(time() - start))
