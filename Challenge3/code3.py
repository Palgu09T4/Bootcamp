# Program to calculate discount on the total amount

# Read total amount from the user
total_amount = float(input("Enter total amount: "))

# Read discount percentage
discount_percentage = float(input("Enter discount percentage: "))

# Calculate discount amount
discount = (total_amount * discount_percentage) / 100

# Calculate final amount after discount
final_amount = total_amount - discount

# Display the results
print("Discount =", discount)
print("Final Amount =", final_amount)
