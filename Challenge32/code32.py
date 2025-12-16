# Coding Challenge 32
# Program to enforce minimum purchase requirement

# Input final grand total
grand_total = float(input("Enter Final Grand Total: "))

# Minimum purchase requirement
minimum_purchase = 500

# Check if minimum purchase is met
if grand_total < minimum_purchase:
    print(f"Minimum purchase of ₹{minimum_purchase} not met. Invoice cannot be generated.")
else:
    print("Minimum purchase met. Invoice can be generated.")
    print(f"Final Grand Total: ₹{grand_total}")
