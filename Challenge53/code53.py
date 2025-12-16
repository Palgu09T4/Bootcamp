# Coding Challenge 53
# Sort array in ascending or descending order

# Input size of array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

# Input sort order
order = input("Enter sorting order (asc/desc): ").lower()

# Sort based on user choice
if order == "asc":
    arr.sort()
    print("Sorted Array (Ascending):", arr)
elif order == "desc":
    arr.sort(reverse=True)
    print("Sorted Array (Descending):", arr)
else:
    print("Invalid sorting order")
