# Project Euler Problem 22

# imports
from time import time
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Measure runtime
start = time()

# Solution
alphabet = 'abcdefghijklmnopqrstuvwxyz'
values = [ord(char) - 96 for char in alphabet.lower()]
alphabet_dict = dict(zip(list(alphabet), values))

f = open('names.txt')
names = sorted(f.read().split(','))
total = 0

for i, name in enumerate(names):
    name = name.strip("\"")
    name_value = 0

    for letter in name:
        name_value += alphabet_dict[letter.lower()]
    
    name_value *= i + 1
    total += name_value

print(total)

# Print runtime
print("--- %.2f seconds ---" %(time() - start))
