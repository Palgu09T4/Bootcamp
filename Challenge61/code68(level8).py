# Patient Details
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
contact = input("Enter Contact Number: ")

# Services and Costs (pre-configured/admin)
services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

GST_RATE = 0.18

print("\nAvailable Services:")
for i in range(len(services)):
    print(f"{i+1}. {services[i]} - ₹{costs[i]}")

# Patient selects services
choices = input("\nEnter service numbers separated by comma: ")
choice_list = choices.split(",")

selected_services = []
selected_costs = []

for ch in choice_list:
    index = int(ch.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
        selected_costs.append(costs[index])

# Calculate subtotal
subtotal = sum(selected_costs)
discount = 0

# Senior Citizen Discount (10% if age >= 60)
if age >= 60:
    senior_discount = subtotal * 0.10
    discount += senior_discount
else:
    senior_discount = 0

# High-Bill Discount (5% if subtotal > 5000 after senior discount)
subtotal_after_senior = subtotal - senior_discount
if subtotal_after_senior > 5000:
    high_bill_discount = subtotal_after_senior * 0.05
    discount += high_bill_discount
else:
    high_bill_discount = 0

subtotal_after_discount = subtotal - discount
gst_amount = subtotal_after_discount * GST_RATE
grand_total = subtotal_after_discount + gst_amount

# Display Invoice
print("\nSelected Services:", selected_services)
print("Selected Costs   :", selected_costs)
print(f"Subtotal             : ₹{subtotal}")
print(f"Senior Citizen Discount : ₹{senior_discount}")
print(f"High-Bill Discount       : ₹{high_bill_discount}")
print(f"Total Discount           : ₹{discount}")
print(f"Subtotal After Discount  : ₹{subtotal_after_discount}")
print(f"GST (18%)                : ₹{gst_amount}")
print(f"Grand Total              : ₹{grand_total}")