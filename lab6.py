# Task 1: Create the Vehicle class
class Vehicle:
    """Vehicle Specs"""

    # Set up the vehicle attributes
    def __init__(self, make, model, year, max_fuel=7.4):
        self.make = make
        self.model = model
        self.year = year
        self.max_fuel = max_fuel
        self.current_fuel = 0
        self.is_almost_empty = True

    # Set the fuel level if the amount is valid
    def fuel_level(self, gallons):
        if gallons <= self.max_fuel and gallons >= 0:
            self.current_fuel = gallons

    # Return the vehicle details
    def details(self):
        return f'{self.make}, {self.model}, {self.year}'

    # Calculate the percentage of fuel left
    def fuel_left(self):
        return round((self.current_fuel / self.max_fuel) * 100, 1)

    # Check if the vehicle has less than 10% fuel
    def empty_warning_check(self):
        if self.fuel_left() < 10:
            self.is_almost_empty = True
        else:
            self.is_almost_empty = False


# Task 2a: Create an empty list
show_list = []


# Task 2b: Create four vehicle objects and add them to the list
vehicle1 = Vehicle("Toyota", "Corolla", 2020, 13.2)
vehicle2 = Vehicle("Honda", "Civic", 2019, 12.4)
vehicle3 = Vehicle("Ford", "Escape", 2022, 15.7)
vehicle4 = Vehicle("Hyundai", "Elantra", 2021, 11.5)

show_list.append(vehicle1)
show_list.append(vehicle2)
show_list.append(vehicle3)
show_list.append(vehicle4)


# Task 2c: Set the fuel levels
vehicle1.fuel_level(5.3)
vehicle2.fuel_level(2.2)
vehicle3.fuel_level(10.1)
vehicle4.fuel_level(0.5)


# Task 2d: Try to set an invalid negative fuel level
vehicle2.fuel_level(-4.4)


# Task 2e: Try to set an invalid fuel level above max fuel
vehicle4.fuel_level(100)


# Task 2f: Display each vehicle's information
for vehicle in show_list:
    vehicle.empty_warning_check()

    print(vehicle.details())
    print(f"Fuel level: {vehicle.current_fuel}")
    print(f"Fuel left: {vehicle.fuel_left()}%")
    print(f"Almost empty: {vehicle.is_almost_empty}")
    print()

    