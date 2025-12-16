# Coding Challenge 55
# Create a 2D array and display elements row-wise

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

# Display matrix row-wise
print("2D Array (Row-wise):")
for row in matrix:
    print(row)
