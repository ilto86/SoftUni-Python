# class Robot:
#     SENSORS = 1
#
#     def __init__(self, name):
#         self.name = name
#
#     def __ad__(self, other):
#         return self.SENSORS + other.SENSORS
#
#     def __len__(self):
#         return len(self.name)
#
#     def __eq__(self, other):
#         self.other = other
#         return self.SENSORS == self.other.SENSORS and self.name == self.other.name
#
#
#     def __gt__(self, other):
#         return self.SENSORS > other.SENSORS
#
# class MedicalRobot(Robot):
#     SENSORS = 6
#
#
# class ChefRobot(Robot):
#     SENSORS = 4
#
#
# class WarRobot(Robot):
#     SENSORS = 12
#
#
# def number_of_robot_sensors(robot):
#     print(robot.SENSORS)
#
#
# class PersonalRobot(Robot):
#     pass
#
#
#
# basic_robot = Robot('Robo')
# da_vinci = MedicalRobot('Da Vinci')
# test_med = MedicalRobot("Da Vinci")
# moley = ChefRobot('Moley')
# griffin = WarRobot('Griffin')
#
#
# print("===" * 50)
# print(da_vinci.SENSORS, test_med.SENSORS)
# print(da_vinci.name, test_med.name)
# print("===" * 50)
# print('Da Vinci is Medical Robot "class.attribut SENSORS" + Moley Chef Robot "class.attribut SENSORS"   here with "Dunder __add__ Method" ')
# print(da_vinci.SENSORS + moley.SENSORS)
# print("===" * 50)
# print('Da Vinci is Medical Robot "class.attribut SENSORS" ="is equal with"= Test Med Medical Robot "class.attribut SENSORS"    "here with Dunder __eq__ Method" ')
# print(da_vinci.SENSORS == test_med.SENSORS)
# print("===" * 50)
# print('Da Vinci is Medical Robot "class.attribut name" ="is equal with"= Test Med Medical Robot "class.attribut name"     "here with Dunder __eq__ Method" ')
# print(da_vinci.name == test_med.name)
# print("===" * 50)
# print('Da Vinci is Medical Robot')
# print(f"Object ID in ours Memory RAM ---> {id(da_vinci)}")
# print("===" * 50)
# print('Test Med Medical Robot')
# print(f"Object ID in ours Memory RAM ---> {id(test_med)}")
# print("===" * 50)
# print('Da Vinci is Medical Robot "Object"   " == is equal with == "   Test Med Medical Robot "Object"      "here with Dunder __eq__ Method" ')
# print(da_vinci == test_med)
# print("===" * 50)
# print('Da Vinci is Medical Robot "Object"   " == is equal with == "   Moley Chef Robot "Object"            "here with Dunder __eq__ Method" ')
# print(da_vinci == moley)
# print("===" * 50)
# print('Da Vinci is Medical Robot "class.attribut SENSORS" here we use SENSORS  > is greater than from >  Test Med Medical Robot "SENSORS"   "with Dunder __gt__ Method" ')
# print(da_vinci > test_med)
# print("===" * 50)
# print('Griffin is War Robot "class.attribut SENSORS" here we use SENSORS   > is greater than from >    Test Med Medical Robot "SENSORS"     "with Dunder __gt__ Method" ')
# print(griffin > test_med)
# print("===" * 50)
# print('Griffin is War Robot "class.attribut SENSORS" here we use SENSORS   > is greater than from >    Test Med Medical Robot "SENSORS"     "with Dunder __gt__ Method" ')
# print(griffin < test_med)
# print("===" * 50)

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Cannot set name less than 2 chars")
        self.__name = value


class Dog(Animal):
    def make_sound(self):
        return "bau bau"


class Cat(Animal):
    def __init__(self, name, laziness):
        super().__init__(name)
        self.laziness = laziness

    def make_sound(self):
        return "meow"


# a = Animal("asd")
# print(a)

a = Cat("asd", 10)
b = Dog("asd")

animals = [a, b]

for animal in animals:
    print(animal.make_sound())

print(a)
print(b)

