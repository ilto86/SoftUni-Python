# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self, distance):
#         pass
#
#     @abstractmethod
#     def refuel(self, fuel):
#         pass
#
#
# class Car(Vehicle):
#     FUEL_CONSUMPTION = 0.9
#
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     def drive(self, distance):
#         driving = self.fuel_quantity - (self.fuel_consumption + self.FUEL_CONSUMPTION) * distance
#         if driving >= 0:
#             self.fuel_quantity -= (self.fuel_consumption + self.FUEL_CONSUMPTION) * distance
#             return self.fuel_quantity
#         return self.fuel_quantity
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel
#         return self.fuel_quantity
#
#
# class Truck(Vehicle):
#     FUEL_CONSUMPTION = 1.6
#     FUEL_QUANTITY = 0.95
#
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     def drive(self, distance):
#         driving = self.fuel_quantity - (self.fuel_consumption + self.FUEL_CONSUMPTION) * distance
#         if driving >= 0:
#             self.fuel_quantity -= (self.fuel_consumption + self.FUEL_CONSUMPTION) * distance
#             return self.fuel_quantity
#         return self.fuel_quantity
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel * self.FUEL_QUANTITY
#         return self.fuel_quantity
#
#
# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
# '''
# Expected Output:    2.299999999999997
#                     12.299999999999997
# '''
#
# print("===" * 50)
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
#
# '''
# Expected Output:    17.0
#                     64.5
# '''




from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.FUEL_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_CONSUMPTION = 1.6
    FUEL_QUANTITY = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.FUEL_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * self.FUEL_QUANTITY)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

print("===" * 50)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)