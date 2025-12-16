# Coding Challenge 56
# Compute the sum of all elements in a 2D array

# Input number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initialize matrix
matrix = []

# Input elements
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
    matrix.append(row)

# Compute sum
total_sum = 0
for row in matrix:
    for value in row:
        total_sum += value

# Display result
print("Sum of all elements:", total_sum)
