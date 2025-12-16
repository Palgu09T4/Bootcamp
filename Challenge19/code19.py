# Coding Challenge 19
# Program to display the series 4, 16, 36, 64 ... N
# (Squares of even numbers)

def even_square_series(N):
    for i in range(2, int(N**0.5) + 1, 2):
        square = i * i
        if square <= N:
            print(square, end=" ")

# Driver code
N = int(input("Enter the value of N: "))
even_square_series(N)
