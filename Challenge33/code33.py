# Coding Challenge 33
# Program to calculate loyalty points based on grand total

# Input final grand total
grand_total = float(input("Enter Final Grand Total: "))

# Calculate loyalty points
loyalty_points = int(grand_total // 100)

# Display result
print("Final Grand Total: ₹", round(grand_total, 2))
print("Loyalty Points Earned:", loyalty_points)
