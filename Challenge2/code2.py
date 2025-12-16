# Program to calculate Simple Interest
# Formula: Simple Interest = (Principal × Rate × Time) / 100

# Read input values from the user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print("Simple Interest =", simple_interest)
