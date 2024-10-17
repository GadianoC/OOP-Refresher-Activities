
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):

    def move(self):
        return 'The car is driving'
    # Implement the move method for the Car class

class Bicycle(Vehicle):

    def move(self):
        return 'the bicycle is pedaling'
    # Implement the move method for the Bicycle class

class Boat(Vehicle):

    def move(self):
        return 'the boat is sailing'
    # Implement the move method for the Boat class

def start_vehicle(vehicle):
    print(vehicle.move())
    # Call the move method of the given vehicle object and print the returned string

# Test your implementation
car = Car()
bicycle = Bicycle()
boat = Boat()

start_vehicle(car)
start_vehicle(bicycle)
start_vehicle(boat)