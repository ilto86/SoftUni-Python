# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person_dict = {"name": "Ines", "age": 27}
#
# person_1 = Person("Ines", 27)
# person_2 = Person("Ivaylo", 32)
#
# print(f'{"-" * 20} Class')
# print(person_1.name)
# print(person_1.age)
# print(f'{"-" * 20} Class')
# print("-" * 50)
# print(f'{"-" * 20} Dictionary')
# print(person_dict["name"])
# print(person_dict["age"])
# print(f'{"-" * 20} Dictionary')



# class Person:
#     def greet(self):
#         return "Hello World"
#
# person = Person()
# print(type(person))
# print(person.greet())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def cebrate_birthday(self):
#         self.age += 1
#         return f"{self.name} is now {self.age}"
#
# person = Person("Ines", 27)
# print(person.age)
# print(person.cebrate_birthday())
# print(person.cebrate_birthday())
# print(person.cebrate_birthday())
# print(person.cebrate_birthday())
# print(person.cebrate_birthday())
# print(person.age)
# print(person.age)
# print(Person.cebrate_birthday(person))
# print(person.age)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        return f"{self.name} сега е на {self.age}"

    def __str__(self):
        return f"Аз съм Куче и се казвам {self.name} и съм на {self.age} години"


x = Dog("Шаро", 3)

print(f'{"-" * 20} String and Dictionary')
print(x)
print(x.__dict__)
print(x.name, x.age)
print("-" * 50)

print(f'{"-" * 20} String and Dictionary')
print(x.celebrate_birthday())
print(x)
print(x.__dict__)
print(x.name, x.age)
print("-" * 50)

print(f'{"-" * 20} String and Dictionary')
print(x.celebrate_birthday())
print(x)
print(x.__dict__)
print(x.name, x.age)
print("-" * 50)

print(x.__str__())