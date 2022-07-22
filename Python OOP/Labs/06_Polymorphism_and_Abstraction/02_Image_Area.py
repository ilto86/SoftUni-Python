class ImageArea:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    # def __lt__(self, other):
    #     return self.get_area() < other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    # def __le__(self, other):
    #     return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    # def __ne__(self, other):
    #     return self.get_area() != other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

print("===" * 50)
print(f"a1 = {a1.get_area()}")
print(f"a2 = {a2.get_area()}")
print("a1 == a2")
print(a1 == a2)
print("===" * 50)
print(f"a1 = {a1.get_area()}")
print(f"a3 = {a3.get_area()}")
print("a1 != a3")
print(a1 != a3)
print("===" * 50)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

print("===" * 50)
print(f"a1 = {a1.get_area()}")
print(f"a2 = {a2.get_area()}")
print("a1 != a2")
print(a1 != a2)

print("===" * 50)
print(f"a1 = {a1.get_area()}")
print(f"a3 = {a3.get_area()}")
print("a1 >= a3")
print(a1 >= a3)
print("===" * 50)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

print(f"a1 = {a1.get_area()}")
print(f"a2 = {a2.get_area()}")
print("a1 <= a2")
print(a1 <= a2)
print("===" * 50)
print(f"a1 = {a1.get_area()}")
print(f"a3 = {a3.get_area()}")
print("a1 < a3")
print(a1 < a3)
print("===" * 50)

