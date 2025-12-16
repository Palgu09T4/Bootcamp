# Coding Challenge 36
# Print number increasing pattern

# Input N
N = int(input("Enter the number of rows: "))

# Loop through rows
for i in range(1, N + 1):
    print(str(i) * i)
