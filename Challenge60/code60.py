# Coding Challenge 60
# Matrix Multiplication

r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    A = []
    B = []

    print("Enter elements of Matrix A:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        A.append(row)

    print("Enter elements of Matrix B:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        B.append(row)

    # Result matrix
    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(row)
