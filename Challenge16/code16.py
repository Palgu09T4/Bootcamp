# Program to validate employee salary inputs

import re

# Function to validate name
def validate_name(name):
    if not name.isalpha() or len(name) > 50:
        return False
    return True

# Function to validate Employee ID
def validate_empid(emp_id):
    if not re.match(r'^[A-Za-z0-9]{5,10}$', emp_id):
        return False
    return True

# Function to validate positive numeric input with max limit
def validate_salary(value, max_value, allow_zero=False):
    try:
        val = float(value)
        if allow_zero:
            if val < 0 or val > max_value:
                return False
        else:
            if val <= 0 or val > max_value:
                return False
        return True
    except:
        return False

# Function to validate bonus percentage
def validate_bonus(value):
    try:
        val = float(value)
        if 0 <= val <= 100:
            return True
        return False
    except:
        return False

# Input with validation
while True:
    name = input("Enter Employee Name: ")
    if validate_name(name):
        break
    print("Invalid name! Only alphabets allowed, max 50 characters.")

while True:
    emp_id = input("Enter Employee ID: ")
    if validate_empid(emp_id):
        break
    print("Invalid EmpID! Alphanumeric, 5–10 characters only.")

while True:
    basic_salary = input("Enter Basic Monthly Salary: ")
    if validate_salary(basic_salary, 10000000, allow_zero=False):
        basic_salary = float(basic_salary)
        break
    print("Invalid Basic Salary! Must be positive and <= 1,00,00,000.")

while True:
    special_allowances = input("Enter Special Allowances: ")
    if validate_salary(special_allowances, 10000000, allow_zero=True):
        special_allowances = float(special_allowances)
        break
    print("Invalid Special Allowances! Must be >=0 and <= 1,00,00,000.")

while True:
    bonus_percent = input("Enter Bonus Percentage: ")
    if validate_bonus(bonus_percent):
        bonus_percent = float(bonus_percent)
        break
    print("Invalid Bonus! Must be numeric between 0 and 100.")

# Derived Calculations
gross_monthly = basic_salary + special_allowances
if gross_monthly <= 0:
    print("Error: Gross Monthly Salary must be greater than zero.")
else:
    annual_gross = (gross_monthly * 12) + (bonus_percent / 100 * gross_monthly * 12)
    if annual_gross > 100000000:
        print("Error: Annual Gross Salary exceeds realistic limit.")
    else:
        print("\nAll inputs valid!")
        print(f"Gross Monthly Salary: Rs. {gross_monthly:,.2f}")
        print(f"Annual Gross Salary: Rs. {annual_gross:,.2f}")
