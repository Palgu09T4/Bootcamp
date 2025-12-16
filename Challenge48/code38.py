# Coding Challenge 48
# Find maximum value in an array

# Input size of array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Find maximum value
if n > 0:
    maximum = max(arr)
    print("Maximum value:", maximum)
else:
    print("Array is empty")
