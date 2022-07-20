# my_dict = {}
# my_list = []
# my_tuple = ()
#
# print(type(my_dict))
# print(type(my_list))
# print(type(my_tuple))
#
# my_list = [200, 100, 50]
# print(my_list[1])
#
# my_dict = {"котка": "cat", "куче": "dog"}
# print(my_dict["куче"])


# people = {1: "Test Testov", 2: "Test 2 Testov", 1: "Ines", 1: "Final"}
#
# print(people[1])


# people = dict({"Name": "George", "Age" : 5}, Sex="M")
# print(people)

# people = {"Name": "George", "Age" : 5}
# people["Sex"] = "M"
# print(people)

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# dict_zipped = dict(zip(keys, values))
# print(dict_zipped)

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# print(dict(zip(keys, values)))

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# print(dict(zip(values, keys)))

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# my_dict = {}
#
# for index in range(len(keys)):
#     my_dict[keys[index]] = values[index]
# print(my_dict)


# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
# print(classes["b"][2])

# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
# print(classes.get("c"))

# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}

# names_a = classes["a"]
# print(names_a[-1])
# names_a.append("ILTO")
# print(names_a[-1])
# print(classes)
# names_b = classes["b"]
# print(names_b[-1])
# names_b.append("Hyulya")
# print(names_b[-1])
# print(classes)

# my_dict = {1: "1", 2: "2"}
#
# res = my_dict[1]
# res = res + "2"
# print(res)
# print(my_dict)
# my_dict[1] = res
# print(my_dict)
# res += "1"
# print(res)
# print(my_dict)
# my_dict[1] = res
# print(my_dict)



# my_dict = {1: 1, 2: 2}
#
# res = my_dict[1]
# res = res + 2
# print(res)
# print(my_dict)
# res += 1
# print(res)
# print(my_dict)



# my_dict = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5}
# print(my_dict)
# for key in my_dict:    #  for key in my_dict.keys():
#     my_dict[key] *= 2
#
# print(my_dict)
# print(my_dict.values())
# for key, value in my_dict.items():
#     print(key, end=" --> ")
#     print(value, end=" = ")
#     print(key, value)


# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# print(classes.keys())
# print(classes.values())
# print(classes.items())


# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# for key in classes:
#     print(key)



# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# for key in classes:
#     print(key)
#     print(classes[key])



# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# for value in classes.values():
#     print(value)


# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# for item in classes.items():
#     print(item)


# a, b = [1, 2]
# print(a)
# print(b)

# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# for key, value in classes.items():
#     print(key, value)



# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# for key in classes:
#     classes[key].append("From the loop")
# print(classes)


# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"]}
#
# classes["a"].append("Testosteron")
# classes["b"].append("Kartof")
# print(classes)



# classes = {"a" : ["Ines", "Georgi", "Test"], "b" : ["Hasan", "Mustafa", "Kemal"], "c": "Pablo Escobar"}
#
# if "Pablo Escobar" in classes.values():
#     print(f"In Dictionary Value Pablo Escobar {classes.values()}")
# if "Test" in classes["a"]:
#     print(f"In Dictionary Value 'Test' is in Key a: {classes['a']}")
# if "a" in classes:
#     print(f"In Dictionary Key a is this List part of Value: {classes['a']}")
# if "b" in classes:
#     print(f"In Dictionary Key b is this List part of Value: {classes['b']}")
# else:
#     print("Nothing in Dictionary")


# a = {1: "A", 2: "B", 3: "C"}
# b =  {"A":1, "B": 2, "C": 3}
# a.pop(2)
# b.pop("A")
# print(a)
# print(b)
# a.popitem()
# b.popitem()
# print(a)
# print(b)
# del a[1]
# del b["B"]
# print(a)
# print(b)




# my_dict = {"Peter": 21, "George": 18, "John": 45}
#
# print(my_dict)
#
# print(sorted(my_dict)) # Сортирва само Ключа и само него изпринтирва
# print(sorted(my_dict.items(), key=lambda x: x[0])) # Сортирва по Ключа
# print(sorted(my_dict.items(), key=lambda x: x[0], reverse=True)) # Сортирва по Ключа НА ОБРАТНО
#
# print(sorted(my_dict.items(), key=lambda x: x[1])) # Сортирва по Стойностите
# print(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)) # Сортирва по Стойностите НА ОБРАТНО
# print(sorted(my_dict.items(), key=lambda x: -x[1])) # Сортирва по Ключа НА ОБРАТНО
#
# num_dict = {1: 20, 2: 5, 4: 75, 5: 60, 3: 55}
#
# print(num_dict)
#
# print(sorted(num_dict))
# print(sorted(num_dict.items(), key=lambda x: x[0])) # Сортирва по Ключа
# print(sorted(num_dict.items(), key=lambda x: -x[0])) # Сортирва по Ключа НА ОБРАТНО
#
# print(sorted(num_dict.items(), key=lambda x: x[1])) # Сортирва по Стойностите
# print(sorted(num_dict.items(), key=lambda x: -x[1])) # Сортирва по Ключа НА ОБРАТНО



# my_dict = {"Peter": 21, "George": 18, "John": 45}
#
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
# print(my_dict)
# print(sorted_dict)
# for key, value in sorted_dict:
#     print(f"Key is {key} and Value is {value}")



# my_dict = {"C": 40, "D": 30, "A": 20, "B": 10}
# print(my_dict)
# sorted_dict = sorted(my_dict.items(), key=lambda x: (x[0], x[1]))
# print(sorted_dict)
# sorted_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))
# print(sorted_dict)

# ------------------------------------  NESTED DICTIONARY  -------------------------------------------------------------

# students = {1: {"name": "Peter", "age": 22}, 2:{"name": "Alex", "age": 21}}
# print(students
#       )
# first_student_name = students[1]["name"]
# first_student_age = students[1]["age"]
# print(first_student_name, end=" is ")
# print(first_student_age)
#
# second_student_name = students[2]["name"]
# second_student_age = students[2]["age"]
# print(second_student_name, end=" --> ")
# print(second_student_age)
#
# students[3] = {}
# students[3]["name"] = "Amy"
# students[3]["age"] = 25
# print(students)
#
# third_student_name = students[3]["name"]
# third_student_age = students[3]["age"]
# print(third_student_name, end="'s age is ")
# print(third_student_age)




# --------------------------------------------  DICTIONARY COMPREHENSION  -------------------------------------------------

# data = [("Peter", 22), ("Amy", 18), ("George", 35)]
# print(dict(data))
# dictionary_data = dict(data)
# print(dictionary_data)
# dictionary = {key:value for (key, value) in data}
# print(dictionary)
#
# even_years1 = {}
# for key, value in dictionary.items():
#     if value % 2 == 0:
#         even_years1[key] = value
# print(even_years1)
# print({key: value for key, value in dictionary.items() if value % 2 == 0})
#
# even_years2 = {}
# for key, value in dictionary.items():
#     if value % 2 == 0:
#         even_years2[value] = key
# print(even_years2)
# print({value: key for key, value in dictionary.items() if value % 2 == 0})



# nums = [1, 2, 3, 4]
# quadrats = {x : x  ** 2 for x in nums}
# cubes = {num:num ** 3 for num in nums}
# print(quadrats)
# print(cubes)

# x = 10
# y = 5
# x = x ^ y
# y = y ^ x
# print(x, y)





#  ----------------------------------List Manipulation with Comprehension ----------------------------------------------
# 1048, 1083, 1090, 1077, 1088
# 1042, 1077, 1088, 1086, 1085, 1080, 1082, 1072

# characters = input().split(", ")
# characters1 = input().split(", ")
# characters_list = [chr(int(x)) for x in characters]
# characters1_list = [chr(int(x)) for x in characters1]
# print(characters_list)
# print(characters1_list)
# print("".join(characters_list))
# print("".join(characters1_list))

#  ----------------------------------Dictionary Manipulation with Comprehension ----------------------------------------------
# 1048, 1083, 1090, 1077, 1088
# 1042, 1077, 1088, 1086, 1085, 1080, 1082, 1072

# characters = input().split(", ")
# characters1 = input().split(", ")
# characters_dict = {x: chr(int(x)) for x in characters}
# characters1_dict = {x: chr(int(x)) for x in characters1}
# print(characters_dict)
# print(characters1_dict)
# for k, v in characters_dict.items():
#     print(v, end="")
# print()
# for key, value in characters1_dict.items():
#     print(value, end="")