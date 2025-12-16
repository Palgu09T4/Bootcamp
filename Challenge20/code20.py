# Coding Challenge 20
# Program to display the series 1, 2, 4, 7, 11, 16, 22 ... N

def series_20(N):
    num = 1
    diff = 1
    while num <= N:
        print(num, end=" ")
        diff += 1
        num += diff

# Driver code
N = int(input("Enter the value of N: "))
series_20(N)
