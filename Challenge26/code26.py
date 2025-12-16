# Coding Challenge 25
# Program to calculate total cost of a single item

# Input item details
item_code = input("Enter Item Code: ")
description = input("Enter Item Description: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Item: "))

# Calculate total cost
total_cost = quantity * price

# Display result
print("\n----- Item Bill -----")
print("Item Code:", item_code)
print("Description:", description)
print("Quantity:", quantity)
print("Price per Item:", price)
print("Total Cost:", total_cost)
