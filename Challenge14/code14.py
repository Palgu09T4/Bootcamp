# Program to calculate net salary after tax deductions

# Accept annual gross salary and total tax payable
annual_gross = float(input("Enter Annual Gross Salary (Rs.): "))
total_tax = float(input("Enter Total Tax Payable (Rs.): "))

# Calculate net salary
net_salary = annual_gross - total_tax

# Display results
print("\nSalary Details:")
print("Annual Gross Salary: Rs.", annual_gross)
print("Total Tax Payable (including cess): Rs.", total_tax)
print("Annual Net Salary: Rs.", net_salary)
