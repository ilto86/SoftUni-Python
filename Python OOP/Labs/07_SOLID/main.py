# class StudentTaxes:
#     def __init__(self, name, semester_tax, average_grade):
#         self.name = name
#         self.semester_tax = semester_tax
#         self.average_grade = average_grade
#
#     def get_discount(self):
#         if self.average_grade > 5:
#             return self.semester_tax * 0.4
#
#
# class AdditionalDiscount(StudentTaxes):
#     def get_discount(self):
#         result = ().get_discount()
#         if result:
#             return result
#         if 4 < self.average_grade <= 5:
#             return self.semester_tax * 0.2
#
#
#
# discount = AdditionalDiscount("Test", 200, 4.68)
# print(discount.get_discount())



from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class ICircleDrawable:
    @staticmethod
    def draw_circle(r):
        print(f"Drawing circle {'O' * r} with radius {r}")


class IRectangleConsoleDrawable:
    @staticmethod
    def draw_top(n):
        print('-' * n)

    @staticmethod
    def draw_side(b, a):
        for _ in range(b):
            print("|" + " "*(a-2) + "|")

    @staticmethod
    def draw_rectangle(a, b):
        IRectangleConsoleDrawable.draw_top(a)
        IRectangleConsoleDrawable.draw_side(b, a)
        IRectangleConsoleDrawable.draw_top(a)


class Rectangle(Shape, IRectangleConsoleDrawable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        IRectangleConsoleDrawable.draw_rectangle(self.a, self.b)


class Circle(Shape, ICircleDrawable):
    def __init__(self, r):
        self.r = r

    def draw(self):
        ICircleDrawable.draw_circle(self.r)


def draw_object(objects):
    for object in objects:
        object.draw()

rect = Rectangle(4, 5)
circle = Circle(5)

draw_object([rect, circle])