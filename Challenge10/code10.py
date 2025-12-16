# Program to generate student report card

# Accept student details
name = input("Enter student name: ")
sub1 = float(input("Enter marks in Subject 1: "))
sub2 = float(input("Enter marks in Subject 2: "))
sub3 = float(input("Enter marks in Subject 3: "))

# Calculate total and average
total = sub1 + sub2 + sub3
average = total / 3

# Determine class secured
if average >= 60:
    result = "1st Class"
elif average >= 50:
    result = "2nd Class"
elif average >= 35:
    result = "Pass Class"
else:
    result = "Fail"

# Display report
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Class Secured:", result)
