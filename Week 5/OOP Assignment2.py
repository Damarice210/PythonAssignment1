# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move method.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Function to demonstrate polymorphism
def describe_movement(vehicle):
    vehicle.move()

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Using polymorphism to call move() on different vehicles
vehicles = [car, plane, boat]
for vehicle in vehicles:
    describe_movement(vehicle)
