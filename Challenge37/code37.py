# Coding Challenge 37
# Print number increasing pattern

# Input N
N = int(input("Enter the number of rows: "))

# Loop through rows
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
