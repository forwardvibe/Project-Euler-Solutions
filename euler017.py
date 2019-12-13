# Project Euler Problem 17

# imports
from time import time
import inflect

# Measure runtime
start = time()

# Variables
total = 0
p = inflect.engine()

# Solution
for n in range(1, 1001):
    word = p.number_to_words(n)
    word = word.replace(" ", "")
    word = word.replace("-", "")
    total += len(word)

print(total)

# Print runtime
print("--- %s seconds ---" %(round(time() - start, 2)))
