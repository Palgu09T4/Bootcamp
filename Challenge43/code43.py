# Coding Challenge 43
# Separate whole and fractional part of a number

# Input a float number
num = float(input("Enter a number: "))

# Separate whole and fractional part
whole_part = int(num)
fractional_part = num - whole_part

# Display results
print("Whole part:", whole_part)
print("Fractional part:", round(fractional_part, 3))  # Rounded to 3 decimals
