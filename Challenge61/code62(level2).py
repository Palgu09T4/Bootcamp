
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

print("Available Services:")
for i in range(len(services)):
    print(f"{i+1}. {services[i]}")

choices = input("\nEnter service numbers separated by comma: ")
choice_list = choices.split(",")

selected_services = []

for ch in choice_list:
    index = int(ch.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])

print("\nSelected Services Array:")
print(selected_services)
