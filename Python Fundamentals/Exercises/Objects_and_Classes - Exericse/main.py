class MyPerson:
    value = 50

    def __init__(self, first_name: str, last_name: str, age=18):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.value = 30

    def say_hello(self):
        return f"Hello {self.first_name} {self.last_name}"

    def __str__(self):
        return f"My Name is {self.first_name} {self.last_name} and I'm {self.age} Year old"



object = MyPerson(last_name="Ivanov", first_name="Ivan", age=35)
print(object)
print(object.first_name)
print(object.say_hello())

print(MyPerson.value)   # This is Class Attribute
print(object.value)
object.value += 1       # This is Instance Attribute
print(object.value)

print("=" * 20)

obj2 = MyPerson("Mark", "Bjorg", 40)
print(obj2)
print(obj2.first_name)
print(obj2.say_hello())

print("=" * 20)

obj3 = MyPerson("Stamat", "Kirilov")
print(obj3)
print(obj3.first_name)
print(obj3.say_hello())