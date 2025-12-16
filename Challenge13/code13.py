# Program to calculate tax payable under New Tax Regime (2023) with rebate and cess

# Accept taxable income
taxable_income = float(input("Enter Taxable Income (Rs.): "))

# Initialize tax
tax = 0

# Tax slabs calculation
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

# Add 4% Health and Education Cess
cess = tax * 0.04
total_tax = tax + cess

# Display breakdown
print("\nTax Breakdown:")
print("Tax before rebate: Rs.", round(tax, 2))
print("Health & Education Cess (4%): Rs.", round(cess, 2))
print("Total Tax Payable: Rs.", round(total_tax, 2))
