# Coding Challenge 18
# Program to display the series 1, 3, 5, 7, 9 ... N

def odd_series(N):
    for i in range(1, N + 1, 2):
        print(i, end=" ")

# Driver code
N = int(input("Enter the value of N: "))
odd_series(N)
