# Coding Challenge 45
# Accept n and store elements into an array

# Input size of array
n = int(input("Enter the size of the array: "))

# Initialize empty array
arr = []

# Input n elements
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Display array
print("Array elements:", arr)
