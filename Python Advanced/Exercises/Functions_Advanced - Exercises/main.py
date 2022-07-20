# Advanded Sorting

'''

sorted(iterable, key=None, reverse=False) iterable are list, set, tuple and dictionary


ll = [10, -2, 5, 3]
print(sorted(ll))
print(sorted(ll, reverse= True))


students = {"a": [5, 6], "b": [2, 3, 4]}
print(sorted(students.items(), key=lambda kvpt: len(kvpt[1]),reverse= True)) # "kvpt is Acronym for Key-Value-Tuple"


students = {"a": [5, 6], "b": [2, 3, 4]}
print(sorted(students.items(), key=lambda kvpt: -len(kvpt[1])))




my_dict = {'Peter': 21, 'George': 18, 'John': 45}
print("------- Normal Print-----------")
print(my_dict)
print("------- Sorted Acending Key-----------")
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
print(sorted_dict)
print("------- Sorted Decending Key-----------")
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0], reverse=True))
print(sorted_dict)
print("------- Sorted Acending Value-----------")
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)
print("------- Sorted Decending Value-----------")
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: -x[1]))
print(sorted_dict)

my_dict = {'Peter': 21, 'George': 18, 'John': 45}
print(sorted(my_dict.items(), key=lambda kvpt: kvpt[1], reverse=True))
# -kvpt[1] is same as reverse=True but it used only for integer( or any Numbers)
my_dict = {'Peter': 21, 'George': 18, 'John': 45}
print(sorted(my_dict.items(), key=lambda kvpt: -kvpt[1]))
'''

# Recursion
# This is bad Recursion
#
# def say_hello():
#     print("Hello")
#     say_hello()
#
# say_hello()


# This is good Recursion

# def say_hello(n=5):
#     if n == 0:
#         return
#     print("Hello")
#     say_hello(n-1)
#
# say_hello()






'''---------------- Function Exercise ----------------------'''

