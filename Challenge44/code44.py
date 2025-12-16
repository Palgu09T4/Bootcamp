# Coding Challenge 44
# Reverse a number

# Input number
num = int(input("Enter a number: "))

# Store original number in temp
temp = num
reverse = 0

# Compute reverse
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# Display reversed number
print("Reverse of the number:", reverse)
