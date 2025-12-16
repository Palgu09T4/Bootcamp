# Coding Challenge 31
# Program to apply payment mode rules

# Input grand total
grand_total = float(input("Enter Grand Total: "))

# Input payment mode
payment_mode = input("Enter Payment Mode (cash/card): ")

# Initialize surcharge
surcharge = 0

# Apply surcharge if payment mode is card
if payment_mode.lower() == "card":
    surcharge = grand_total * 0.02
    grand_total += surcharge
    print("Credit Card Surcharge Applied: ₹", round(surcharge, 2))
else:
    print("No Surcharge Applied for Cash Payment")

# Display final payable amount
print("Final Payable Amount: ₹", round(grand_total, 2))
