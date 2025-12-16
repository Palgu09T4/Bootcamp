# Coding Challenge 30
# Program to apply promotional discounts on specific items

# Input for a single item
item_code = input("Enter Item Code: ")
description = input("Enter Item Description: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Item: "))

# Calculate item total
item_total = quantity * price

# Apply promotional discount if applicable
if item_code.upper() == "PROMO10":
    discount = item_total * 0.10
    item_total -= discount
    print("Promotional Discount Applied: ₹", discount)
else:
    discount = 0
    print("No Promotional Discount Applied")

# Display final amount for the item
print("Final Item Total: ₹", item_total)
