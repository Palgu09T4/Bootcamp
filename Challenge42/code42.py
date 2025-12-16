# Coding Challenge 42
# Generate series 1, -5, 9, -13, 17, -21 … up to N terms

# Input N (number of terms)
N = int(input("Enter the number of terms: "))

num = 1  # Starting number
sign = 1  # Initial sign

for i in range(N):
    print(sign * num, end=" ")
    num += 4
    sign *= -1  # Alternate sign
