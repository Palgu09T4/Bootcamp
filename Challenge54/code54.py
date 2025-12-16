# Coding Challenge 54
# Implement Binary Search on the array

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1   # position (1-based index)
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input size of array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

# Sort array (required for binary search)
arr.sort()

# Input element to search
key = int(input("Enter element to search: "))

# Perform binary search
position = binary_search(arr, key)

# Display result
if position != -1:
    print(f"Element {key} found at position {position}")
else:
    print(f"Element {key} not found in the array")
