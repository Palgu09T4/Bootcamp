# Coding Challenge 39
# Pattern of Perfect Squares with Alternating Signs

# Input N
N = int(input("Enter the number of rows: "))

count = 1
for i in range(1, N + 1):
    row = []
    for j in range(i):
        val = count ** 2
        # Apply alternating signs per row
        if (i + j) % 2 != 0:
            val = -val
        row.append(str(val))
        count += 1
    print(" ".join(row))
