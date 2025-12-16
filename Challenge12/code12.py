# Program to calculate taxable income after standard deduction

# Accept annual gross salary
annual_gross = float(input("Enter Annual Gross Salary (Rs.): "))

# Standard Deduction
standard_deduction = 50000

# Calculate taxable income
taxable_income = annual_gross - standard_deduction

# Display results
print("\nSalary Details:")
print("Annual Gross Salary: Rs.", annual_gross)
print("Standard Deduction: Rs.", standard_deduction)
print("Taxable Income: Rs.", taxable_income)
