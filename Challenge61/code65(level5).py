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

print("Available Services:")
for i in range(len(services)):
    print(f"{i+1}. {services[i]} - ₹{costs[i]}")

choices = input("\nEnter service numbers separated by comma: ")
choice_list = choices.split(",")

selected_services = []
selected_costs = []

for ch in choice_list:
    index = int(ch.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
        selected_costs.append(costs[index])

subtotal = sum(selected_costs)
gst_amount = subtotal * GST_RATE
grand_total = subtotal + gst_amount

print("\nSelected Services:", selected_services)
print("Selected Costs   :", selected_costs)
print("Subtotal         : ₹", subtotal)
print("GST (18%)        : ₹", gst_amount)
print("Grand Total      : ₹", grand_total)
