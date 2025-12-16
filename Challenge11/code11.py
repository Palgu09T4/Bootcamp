# Program to calculate employee gross salary

# Accept employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Monthly Salary: "))
special_allowances = float(input("Enter Special Allowances (Monthly): "))
bonus_percent = float(input("Enter Annual Bonus Percentage (%): "))

# Calculate gross monthly salary
gross_monthly = basic_salary + special_allowances

# Calculate annual bonus
annual_bonus = (bonus_percent / 100) * (gross_monthly * 12)

# Calculate annual gross salary
annual_gross = (gross_monthly * 12) + annual_bonus

# Display results
print("\nEmployee Details:")
print("Name:", name)
print("Employee ID:", emp_id)
print("Gross Monthly Salary: Rs.", gross_monthly)
print("Annual Gross Salary (including bonus): Rs.", annual_gross)
