# Coding Challenge 21
# Program to display the series 1, 4, 9, 25, 36, 49, 81 ... N
# (Perfect squares excluding 16 and 64)

def series_21(N):
    i = 1
    while i * i <= N:
        if i != 4 and i != 8:  # skip 16 and 64
            print(i * i, end=" ")
        i += 1

# Driver code
N = int(input("Enter the value of N: "))
series_21(N)
