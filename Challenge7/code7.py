# Program to check tax eligibility based on salary

name = input("Enter name: ")
salary = float(input("Enter salary: "))

if salary > 300000:
    print(name, "must pay tax")
else:
    print(name, "does not need to pay tax")
