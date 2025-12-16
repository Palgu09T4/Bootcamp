services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

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

print("\nSelected Services:", selected_services)
print("Selected Costs   :", selected_costs)
