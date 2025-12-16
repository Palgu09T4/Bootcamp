name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
contact = input("Enter Contact Number: ")

# Step 2: Available Services and Costs
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

GST_RATE = 0.18

print("\nAvailable Services:")
for i in range(len(services)):
    print(f"{i+1}. {services[i]} - ₹{costs[i]}")

# Step 3: Patient selects services
choices = input("\nEnter service numbers separated by comma: ")
choice_list = choices.split(",")

selected_services = []
selected_costs = []

for ch in choice_list:
    index = int(ch.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
        selected_costs.append(costs[index])

# Step 4: Calculate totals
subtotal = sum(selected_costs)
gst_amount = subtotal * GST_RATE
grand_total = subtotal + gst_amount

# Step 5: Display Invoice
print("\n" + "-"*50)
print("HealWell Care Hospital")
print("Patient Invoice")
print("-"*50)
print(f"Patient Information:")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Gender : {gender}")
print(f"Contact: {contact}\n")

print("Services Availed:")
for i in range(len(selected_services)):
    print(f"{i+1}. {selected_services[i]}: ₹{selected_costs[i]}")

print(f"\nSubtotal: ₹{subtotal}")
print(f"GST (18%): ₹{gst_amount}")
print(f"Grand Total: ₹{grand_total}")
print("Thank you for choosing HealWell Care Hospital!")
print("-"*50)
