### SIMPLE TASK 036 ###

"""DONE"""  # Practical Example: Developing Your Own Class

"""DONE"""  # Class Design: Choose a simple concept from your everyday life (e.g., a book, a car, a bank account, a pet) and design a Python class for it.
"""DONE"""  # Ensure your class has at least three meaningful attributes (e.g., title, author, number of pages for a book; brand, model, year of manufacture for a car).
"""DONE"""  # # Implement at least two methods that describe the behavior of your object (e.g., read() and open() for a book; drive() and refuel() for a car).
"""DONE"""  # Use the __init__ method to set the initial values of your attributes.
"""DONE"""  # Create two to three different instances (objects) of your class with different attribute values.
"""DONE"""  # Apply your objects' methods and access their attributes to demonstrate that everything works as expected. Print the results to the console.


class Computer:
    print("\nComputer class created!!!")

    def __init__(self, marke, system, ram):
        self.marke = marke
        self.system = system
        self.ram = ram

    def start(self):
        print(f"{self.marke} is starting!!!")

    def install(self, program):
        print(
            f"The {program} will be installed on the {self.system} of the {self.marke} PC"
        )


pc_1 = Computer("HP", "Windows 11 Pro", 16)

print(f"\npc1_class: {pc_1}")
print(f"pc1_class.marke: {pc_1.marke}")
print(f"pc1_class.sytem: {pc_1.system}")
print(f"pc1_class.ram: {pc_1.ram}\n\n")

Computer.start(pc_1)
Computer.install(pc_1, "WinZIP")


### EXPERT TASK 036 ###
# Blueprint for the Digital World: Classes, Objects, and Interaction
# Imagine you are developing a system for managing vehicle fleets for a logistics company. The company wants to manage various vehicle types, track their status, and perform basic operations.

# Task 2.1: The Base Class Vehicle

import uuid


class Vehicle:
    def __init__(self, brand, model, license_plate):
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.mileage = 0.0
        self.status = "ready"
        self.vehicle_id = str(uuid.uuid4())

    def drive(self, distance_km):
        if self.status != "ready":
            print(f"{self.brand} - {self.model} is not ready")
            return
        else:
            self.mileage += distance_km

    def set_status(self, new_status):
        if (
            new_status == "ready"
            or new_status == "in operation"
            or new_status == "in maintenance"
            or new_status == "decommissioned"
        ):
            self.status = new_status
        else:
            print(f"{new_status} is wrong status")

    def __str__(self):
        return f"Vehicle {self.vehicle_id}: {self.brand} {self.model} ({self.license_plate}), Status: {self.status}, Mileage: {self.mileage}"


auto_1 = Vehicle("BMW", "X1", "PB001")

print("\n\n=== TEST 1: Print object ===")
print(auto_1)

print("\n=== TEST 2: Drive 120 km ===")
auto_1.drive(120)
print(auto_1.mileage)

print("\n=== TEST 3: Status → maintenance, try driving ===")
auto_1.set_status("in maintenance")
auto_1.drive(50)
print(auto_1.status)
print(auto_1.mileage)

print("\n=== TEST 4: Status → ready, drive 30 km ===")
auto_1.set_status("ready")
auto_1.drive(30)
print(auto_1.status)
print(auto_1.mileage)

print("\n=== TEST 5: Wrong status ===")
auto_1.set_status("flying")
print("Current status:", auto_1.status)

print("\n=== TEST 6: UUID check ===")
auto_2 = Vehicle("Mercedes", "Actros", "HH123")
print(auto_1.vehicle_id)

# Task 2.2: Specialized Vehicle Types


class Truck(Vehicle):
    def __init__(self, brand, model, license_plate, max_payload_kg):
        super().__init__(brand, model, license_plate)

        self.max_payload_kg = max_payload_kg
        self.current_load_kg = 0.0

    def load(self, weight_kg):
        if self.current_load_kg + weight_kg <= self.max_payload_kg:
            self.current_load_kg += weight_kg
        else:
            self.current_load_kg = self.max_payload_kg

    def unload(self, weight_kg):
        if self.current_load_kg - weight_kg >= 0:
            self.current_load_kg -= weight_kg
        else:
            self.current_load_kg = 0

    def __str__(self):
        base_info = super().__str__()
        return (
            base_info
            + f", Max Payload: {self.max_payload_kg} kg"
            + f", Current Load: {self.current_load_kg} kg"
        )


print("\n\n=== TEST 1: Create Truck & Print ===")
truck_1 = Truck("Volvo", "FH16", "HH-1234", 20000)
print(truck_1)


print("\n=== TEST 2: Load 5000 kg ===")
truck_1.load(5000)
print(truck_1.current_load_kg)


print("\n=== TEST 3: Load over limit (try 30000 kg) ===")
truck_1.load(30000)
print(truck_1.current_load_kg)


print("\n=== TEST 4: Unload 7000 kg ===")
truck_1.unload(7000)
print(truck_1.current_load_kg)


print("\n=== TEST 5: Unload below zero (try 50000 kg) ===")
truck_1.unload(50000)
print(truck_1.current_load_kg)
