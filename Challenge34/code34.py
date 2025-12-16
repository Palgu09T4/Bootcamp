# Coding Challenge 34
# Print number pattern: 1 to N in N rows

# Input N
N = int(input("Enter the number of rows: "))

# Loop through rows
for i in range(N):
    for j in range(1, N + 1):
        print(j, end="")
    print()
