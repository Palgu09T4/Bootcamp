# Program to swap two numbers

# Read two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap the values using a temporary variable
temp = a
a = b
b = temp

# Display the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
