# Project Euler Problem 6

# Sum of the squares of the first 100 natural numbers
sum_of_squares = sum([x**2 for x in range(1, 101)])

# Square of the sum of the first 100 natural numbers
square_of_sum = sum(range(101))**2

# Output
print(square_of_sum - sum_of_squares)
