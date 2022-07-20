# import math
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calculate_distance(self, point):
#         return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
#
#     @staticmethod
#     def calc_distance(point_1, point_2):
#         return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)
#
#
# p = Point(15, 20)
# p2 = Point(5, 10)
# print(p.calculate_distance(p2))
# print(Point.calc_distance(p, p2))


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
# print(Person.is_adult(5))       # Good Practice
# girl = Person("Amy")
# print(girl.is_adult(20))        # Bad Practice
# boy = Person("Jack")
# print(boy.is_adult(17))         # Bad Practice



# class Laptop:
#     brand = "Mac"
#     def __init__(self, memory, model):
#         self.memory = memory
#         self.model = model
#
#     @classmethod
#     def low_ram_laptop(cls, model):
#         return cls(16, model)
#
#     @classmethod
#     def high_ram_laptop(cls, model):
#         return cls(32, model)
#
#     @classmethod
#     def change_brand(cls):
#         cls.brand = "Changed"
#
#     def __str__(self):
#         return f"Laptop model is {self.model} with ram {self.memory}"
#
#
# laptop_custom = Laptop(8, "Asus")
# print(laptop_custom)
#
# small_ram_laptop = Laptop.low_ram_laptop("Dell")
# print(small_ram_laptop)
#
# laptop2 = Laptop.high_ram_laptop("HP")
# print(laptop2)
#
# print("=" * 50)
#
# print(Laptop.brand)
# Laptop.change_brand()
# print(Laptop.brand)



# class Person:
#     min_age = 0
#     max_age = 150
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def __validate_age(cls, value):
#         if value < Person.min_age or value > Person.max_age:
#             raise ValueError()
#
#     # @property
#     # def is_adult(self):
#     #     return self.__age >= 18
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__validate_age(value)
#         self.__age = value
#
#
# class Employee(Person):
#     min_age = 16
#     max_age = 150
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def __validate_age(value):
#         if value < Employee.min_age or value > Employee.max_age:
#             raise ValueError()
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__validate_age(value)
#         self.__age = value


# p = Person("Test", 2)
# print(p.name)
# print(p.min_age)
# print(p.age)
#
# e = Employee("Test1", 16, 1000)
# print(e.name)
# print(e.min_age)
# print(e.age)
#
# e1 = Employee("Test2", 15, 1001)
# print(e1.name)
# print(e1.min_age)
# print(e1.age)

''' The same but simplified way and optimized way'''

class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def __validate_age(cls, value):
        if value < cls.min_age or value > cls.max_age:
            raise ValueError(f"{value} must be between {cls.min_age} and {cls.max_age}")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):
    min_age = 16

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


p = Person("Test", 2)
print(p.name)
print(p.min_age)
print(p.age)

e = Employee("Test1", 16, 1000)
print(e.name)
print(e.min_age)
print(e.age)

e1 = Employee("Test2", 15, 1001)
print(e1.name)
print(e1.min_age)
print(e1.age)