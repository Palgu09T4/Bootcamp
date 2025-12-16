# Coding Challenge 52
# Reverse the given array

# Input size of array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

# Reverse array
reversed_arr = arr[::-1]

# Display result
print("Reversed Array:", reversed_arr)
