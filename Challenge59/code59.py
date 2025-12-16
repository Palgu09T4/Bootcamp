# Coding Challenge 59
# Store elements into M x N matrix and display matrix and its transpose

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
    matrix.append(row)

print("Original Matrix:")
for row in matrix:
    print(row)

# Transpose
transpose = []
for j in range(cols):
    t_row = []
    for i in range(rows):
        t_row.append(matrix[i][j])
    transpose.append(t_row)

print("Transpose Matrix:")
for row in transpose:
    print(row)
