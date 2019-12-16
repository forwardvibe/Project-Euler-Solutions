# Project Euler Problem 19

# imports
from time import time
from datetime import datetime
from dateutil.relativedelta import *

# Measure runtime
start = time()

# Number of Sundays
total = 0

# Starting date
dt = datetime.strptime("01/01/1901", "%m/%d/%Y")

# Check only the first of every month 01/01/1901 - 12/31/2000
for month in range(12 * (2001 - 1901)):
    
    # Check if Sunday
    if 6 == dt.weekday():
        total += 1
    
    # Iterate to next month
    dt += relativedelta(months=+1)

# Answer
print(total)

# Print runtime
print("--- %s seconds ---" %(round(time() - start, 2)))
