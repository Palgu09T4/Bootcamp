# Coding Challenge 47
# Find minimum value in an array

# Input size of array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Find minimum value
if n > 0:
    minimum = min(arr)
    print("Minimum value:", minimum)
else:
    print("Array is empty")
