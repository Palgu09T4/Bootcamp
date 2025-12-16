# Coding Challenge 33
# Print number pattern: same number repeated N times per row

# Input N
N = int(input("Enter the number of rows: "))

# Loop through rows
for i in range(1, N + 1):
    print(str(i) * N)
