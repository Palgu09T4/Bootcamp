# Coding Challenge 57
# Check if a given element exists in a 2D array

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

# Input element to search
search_element = int(input("Enter element to search: "))

# Search element
found = False
for row in matrix:
    if search_element in row:
        found = True
        break

# Display result
if found:
    print(f"Element {search_element} exists in the 2D array")
else:
    print(f"Element {search_element} does not exist in the 2D array")
