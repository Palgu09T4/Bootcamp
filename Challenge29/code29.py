# Coding Challenge 29
# Program to calculate tax based on grand total

# Input grand total
grand_total = float(input("Enter Grand Total: "))

# Determine tax rate
if grand_total < 5000:
    tax_rate = 0.05
elif grand_total <= 20000:
    tax_rate = 0.10
else:
    tax_rate = 0.15

# Calculate tax
tax = grand_total * tax_rate
grand_total += tax

# Display results
print(f"Tax Applied: ₹{tax:.2f}")
print(f"Final Payable Amount: ₹{grand_total:.2f}")
