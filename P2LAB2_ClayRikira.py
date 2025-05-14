# Name: Rikira Clay
# Date: 03/09/2025
# Assignment Name: Vehicle MPG Dictionary
# Description: This program creates a dictionary of vehicle names and their MPG,
#              extracts the keys, and displays them.

# Create the dictionary
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Extract the keys into a variable
vehicle_names = vehicle_mpg.keys()

# Print the dictionary
print("Vehicle MPG Data:")
for vehicle, mpg in vehicle_mpg.items():
    print(f"{vehicle}: {mpg} MPG")

# Print the keys
print("\nList of vehicle names:")
for name in vehicle_names:
    print(name)
