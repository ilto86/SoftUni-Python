# import re
#
# NAME_SEPARATOR = "[@|]"
# AGE_SEPARATOR = "[#*]"
#
# def read_input(n):
#     result = []
#     for line in range(n):
#         result.append(input())
#     return result
#
# N = int(input()) # num of lines
# input_data = read_input(N)
# for string in input_data:
#     name = re.split(NAME_SEPARATOR, string)[1]
#     age = re.split(AGE_SEPARATOR, string)[1]
#     print(f"{name} is {age} years old.")





# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
#
# lines = [input() for line in range(int(input()))]
# persons = []
# for line in lines:
# 	name = line[line.index("@")+1:line.index("|")]
# 	age = line[line.index("#")+1:line.index("*")]
# 	persons.append(Person(name, age))
#
# for person in persons:
# 	print(f"{person.name} is {person.age} years old.")





for _ in range(int(input())):
    text = input()
    name = ''
    age = ''
    for i in range(len(text)):
        if text[i] == '@':
            for j in range(i + 1, len(text)):
                name += text[j]
                if name[-1] == '|':
                    break
        elif text[i] == '#':
            for j in range(i + 1, len(text)):
                age += text[j]
                if age[-1] == '*':
                    break
    if name[-1] == '|':
        name = name[:-1]
    else:
        name = ''
    if age[-1] == '*':
        age = age[:-1]
    else:
        break
    if not name == '' and not age == '':
        print(f'{name} is {age} years old.')