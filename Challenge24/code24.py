# Coding Challenge 24
# Program to display the Fibonacci series: 1, 1, 2, 3, 5, 8, 13, 21 ... N

def fibonacci_series(N):
    if N < 1:
        return
    
    a, b = 1, 1
    print(a, end=" ")
    
    if N >= 1:
        print(b, end=" ")
    
    while True:
        c = a + b
        if c > N:
            break
        print(c, end=" ")
        a, b = b, c

# Driver code
N = int(input("Enter the value of N: "))
fibonacci_series(N)
