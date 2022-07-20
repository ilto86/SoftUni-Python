# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# test_person = Person("Test Testov", 5)
# ilto = Person("Ilter Zekerie", 35)
# print(test_person.name, test_person.age)
# print(test_person.name)
# print(test_person.age)
# print(ilto.name, ilto.age)
# print(ilto.name)
# print(ilto.age)




# class Party:
#     def __init__(self):
#         self.people = []
#
# my_party = Party()
# your_party = Party()
# third_party = Party()
#
# parties = [my_party, your_party, third_party]
#
# while True:
#     my_party_guest = input()
#     if my_party_guest!= "End":
#         my_party.people.append(my_party_guest)
#     your_party_guest = input()
#     if your_party_guest != "End":
#         your_party.people.append(your_party_guest)
#     third_party_guest = input()
#     if third_party_guest != "End":
#         third_party.people.append(third_party_guest)
#
#     if my_party_guest == "End" or your_party_guest == "End" or third_party_guest == "End":
#         break
#
# print(parties)
#
# print(f"Going: {', '.join(my_party.people)}")
# print(f"Total: {len(my_party.people)}")
#
# print(f"Going: {', '.join(your_party.people)}")
# print(f"Total: {len(your_party.people)}")
#
# print(f"Going: {', '.join(third_party.people)}")
# print(f"Total: {len(third_party.people)}")


# my_party Maria
# your_party Gulaban
# third_party Buhalan
# third_party Sortlan
# your_party Bechirov
# my_party Nikol
# your_party Golemanski
# my_party Silvia
# third_party Gender
# End



# class Party:
#     def __init__(self):
#         self.people = []
#
# my_party = Party()
# your_party = Party()
# third_party = Party()
#
# parties = [my_party, your_party, third_party]
#
# name = input()
#
# while not name == "End":
#     if name == "End":
#         break
#     name = name.split()
#     if name[0] == "my_party":
#         my_party.people.append(name[1])
#     if name[0] == "your_party":
#         your_party.people.append(name[1])
#     if name[0] == "third_party":
#         third_party.people.append(name[1])
#
#     name = input()
#
# print(parties)
#
# print(f"Going: {', '.join(my_party.people)}")
# print(f"Total: {len(my_party.people)}")
#
# print(f"Going: {', '.join(your_party.people)}")
# print(f"Total: {len(your_party.people)}")
#
# print(f"Going: {', '.join(third_party.people)}")
# print(f"Total: {len(third_party.people)}")




# class Person:
#     species = "mammal"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# me = Person("Peter", 25)  # me.species = "mammal"
# you = Person("John", 44)
# print(me.name, you.name)
# print(me.species, you.species)



# class Person:
#     def __init__(self, first_name, last_name, age=18):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def say_hello(self, school):
#         return f"Hello  {self.first_name} {self.last_name} from {school}"
#
# ivan = Person("Ivan", "Ivanov", 25)  # me.species = "mammal"
# georgi = Person("Georgi", "Georgiev")
#
# print(ivan.say_hello("SoftUni"))
# print(georgi.say_hello("SoftUni"))
# print(ivan.first_name, ivan.last_name, ivan.age)
# print(ivan.first_name)
# print(ivan.last_name)
# print(ivan.age)
# print(georgi.first_name, georgi.last_name, georgi.age)
# print(georgi.first_name)
# print(georgi.last_name)
# print(georgi.age)


# class Person:
#     species = "mammal"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# me = Person("Peter", 25)  # me.species = "mammal"
# you = Person("John", 44)
# me.age += 1
# print(me.name, you.name)
# print(me.species, you.species)
# print(me.age)


# class Test:
#     value = 52
#     def __init__(self):
#         self.value = 42
#
# print(Test.value)
# test = Test()



# class Test:
#     value = 52
#     def __init__(self, val1, val2):
#         self.val1 = val1
#         self.val2 = val2
#
#     def sum_numbers(self, val3):
#         return (self.val1 * self.val2) + val3
#
# obj = Test(10, 5)
# print(obj.sum_numbers(5))





