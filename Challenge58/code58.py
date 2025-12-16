# Coding Challenge 58
# Display matrix and its transpose

# Input matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix elements
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
    matrix.append(row)

# Display original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Compute transpose
transpose = []
for j in range(cols):
    t_row = []
    for i in range(rows):
        t_row.append(matrix[i][j])
    transpose.append(t_row)

# Display transpose matrix
print("Transpose Matrix:")
for row in transpose:
    print(row)
