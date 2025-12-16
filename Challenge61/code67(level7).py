# Admin inputs number of services
n = int(input("Enter number of services to configure: "))

services = []
costs = []

for i in range(n):
    service_name = input(f"Enter name of service {i+1}: ")
    service_cost = float(input(f"Enter cost of '{service_name}': ₹"))
    services.append(service_name)
    costs.append(service_cost)

print("\nServices configured successfully!")
print("Services Array:", services)
print("Costs Array   :", costs)
