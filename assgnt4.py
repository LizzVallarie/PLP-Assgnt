# This code demonstrates object-oriented programming concepts in Python:
# - Classes and objects
# - Inheritance
# - Polymorphism
#
# It includes two parts:
# 1. A Smartphone class with an iPhone subclass, showing inheritance and polymorphism.
# 2. Vehicle classes (Car, Plane, Boat) demonstrating polymorphism through the move() method.

### Part 1: Smartphone and iPhone Classes

class Smartphone:
    def __init__(self, brand, model, screen_size, os, storage):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.os = os
        self.storage = storage
        self.battery_level = 100  # Starts fully charged
        self.is_on = False        # Starts off

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now on.")
        else:
            print("The phone is already on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now off.")
        else:
            print("The phone is already off.")

    def make_call(self, number):
        if self.is_on:
            if self.battery_level > 0:
                print(f"Calling {number} from {self.brand} {self.model}.")
                self.battery_level -= 5  # Calling uses 5% battery
            else:
                print("Battery is too low to make a call.")
        else:
            print("The phone is off. Cannot make a call.")

    def unlock(self):
        print("Unlocking with PIN.")

    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")

class iPhone(Smartphone):
    def __init__(self, model, screen_size, storage):
        super().__init__("Apple", model, screen_size, "iOS", storage)
        self.ios_version = "15.0"  # Specific iOS version

    def activate_siri(self):
        if self.is_on:
            print("Hey Siri!")
        else:
            print("The phone is off. Cannot activate Siri.")

    def unlock(self):
        print("Unlocking with Face ID.")

### Demonstration: Smartphone and iPhone

print("\n--- Demonstrating Smartphone and iPhone ---")

# Create a generic Smartphone
generic_phone = Smartphone("Samsung", "Galaxy S21", 6.2, "Android", 128)
generic_phone.turn_on()
generic_phone.unlock()  # Uses PIN
generic_phone.make_call("123-456-7890")
generic_phone.check_battery()
generic_phone.turn_off()

# Create an iPhone
iphone = iPhone("iPhone 13", 6.1, 256)
iphone.turn_on()
iphone.unlock()  # Uses Face ID
iphone.activate_siri()
iphone.make_call("098-765-4321")
iphone.turn_off()

### Part 2: Vehicle Classes

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Moving at {self.speed} km/h.")

class Car(Vehicle):
    def move(self):
        print(f"Driving on the road at {self.speed} km/h.")

class Plane(Vehicle):
    def move(self):
        print(f"Flying in the sky at {self.speed} km/h.")

class Boat(Vehicle):
    def move(self):
        print(f"Sailing on the water at {self.speed} km/h.")

### Demonstration: Vehicle Polymorphism

print("\n--- Demonstrating Vehicle Polymorphism ---")

# Create vehicle instances
car = Car(100)
plane = Plane(800)
boat = Boat(30)

# Demonstrate polymorphism using a list
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle.move()