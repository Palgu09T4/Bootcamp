# Coding Challenge 40
# Pattern of Factorials in N Rows

import math

# Input N
N = int(input("Enter the number of rows: "))

count = 1  # Starting number for factorials
for i in range(1, N + 1):
    row = []
    for j in range(i):
        row.append(str(math.factorial(count)))
        count += 1
    print(" ".join(row))
