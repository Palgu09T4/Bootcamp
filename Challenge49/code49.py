# Coding Challenge 49
# Search for a given element in an array

# Input size of array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Input element to search
search_element = int(input("Enter element to search: "))

# Search for the element
positions = [i + 1 for i, val in enumerate(arr) if val == search_element]

# Display result
if positions:
    print(f"Element {search_element} found at position(s):", positions)
else:
    print(f"Element {search_element} not found in the array")
