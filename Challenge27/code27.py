# Coding Challenge 27
# Program to apply discounts on grand total

# Input values
grand_total = float(input("Enter Grand Total: "))
total_quantity = int(input("Enter Total Quantity: "))

# Apply 10% discount if grand total exceeds 10000
if grand_total > 10000:
    discount1 = grand_total * 0.10
    grand_total -= discount1
    print("10% Discount Applied:", discount1)
else:
    discount1 = 0

# Apply 5% quantity discount if quantity exceeds 20
if total_quantity > 20:
    discount2 = grand_total * 0.05
    grand_total -= discount2
    print("5% Quantity Discount Applied:", discount2)
else:
    discount2 = 0

# Display final amount
print("Final Payable Amount:", grand_total)
