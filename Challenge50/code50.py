# Coding Challenge 50
# Count odd and even numbers in an array

# Input size of array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Initialize counters
even_count = 0
odd_count = 0

# Count odd and even numbers
for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
