# Coding Challenge 28
# Program to apply membership discount

# Input grand total
grand_total = float(input("Enter Grand Total: "))

# Membership input
member = input("Is the customer a member? (y/n): ")

# Apply 2% membership discount
if member.lower() == 'y':
    discount = grand_total * 0.02
    grand_total -= discount
    print("2% Membership Discount Applied:", discount)
else:
    discount = 0
    print("No Membership Discount Applied")

# Display final amount
print("Final Payable Amount:", grand_total)
