from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calc_area(self):
        return self.base * self.height / 2


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()
        return total


shapes = [Square(4), Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
