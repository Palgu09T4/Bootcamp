# Coding Challenge 23
# Program to display the series 1, 5, 9, 13, 21, 25, 29, 37, 41 ... N

def series_23(N):
    num = 1
    print(num, end=" ")

    # Pattern of differences: +4, +4, +4, +8 (repeats)
    diffs = [4, 4, 4, 8]
    i = 0

    while True:
        num = num + diffs[i % 4]
        if num > N:
            break
        print(num, end=" ")
        i += 1

# Driver code
N = int(input("Enter the value of N: "))
series_23(N)
