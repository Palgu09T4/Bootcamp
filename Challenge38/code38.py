# Coding Challenge 38
# Fibonacci Series Pattern

# Input N
N = int(input("Enter the number of rows: "))

# Generate Fibonacci numbers up to required count
fib = [1, 1]
while len(fib) < (N * (N + 1)) // 2:  # Total numbers needed
    fib.append(fib[-1] + fib[-2])

# Print pattern
index = 0
for i in range(1, N + 1):
    for j in range(i):
        print(fib[index], end=" ")
        index += 1
    print()
