# Program to generate detailed employee salary report

# Accept employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Monthly Salary: "))
special_allowances = float(input("Enter Special Allowances (Monthly): "))
bonus_percent = float(input("Enter Annual Bonus Percentage (%): "))

# Step 1: Gross Salary Calculation
gross_monthly = basic_salary + special_allowances
annual_bonus = (bonus_percent / 100) * (gross_monthly * 12)
annual_gross = (gross_monthly * 12) + annual_bonus

# Step 2: Taxable Income Calculation
standard_deduction = 50000
taxable_income = annual_gross - standard_deduction

# Step 3: Tax Calculation based on New Tax Regime 2023
tax = 0
if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = (300000 * 0.05) + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30

# Apply Section 87A Rebate
if taxable_income <= 700000:
    tax = 0

# Add 4% Health & Education Cess
cess = tax * 0.04
total_tax = tax + cess

# Step 4: Net Salary
net_salary = annual_gross - total_tax

# Step 5: Display Report
print("\nEmployee Salary Report")
print("-" * 40)
print(f"Name: {name}")
print(f"Employee ID: {emp_id}")
print(f"Gross Monthly Salary: Rs. {gross_monthly:,.2f}")
print(f"Annual Gross Salary: Rs. {annual_gross:,.2f}")
print(f"Taxable Income: Rs. {taxable_income:,.2f}")
print(f"Tax Payable (with breakdown): Rs. {total_tax:,.2f}")
print(f"Annual Net Salary: Rs. {net_salary:,.2f}")
print("-" * 40)
