# import os
# from io import open
#import io

#io.open()

# file = open('./01_File_Opener.py')

# print(file.read())

# print(os.sep)



# file_path = ".\\text.txt"
#
# file = open(file_path, "r")
# print(file.read())
#
# print("-" * 20)
#
# file = open(file_path, "r")
# print(file.read(2))
# print(file.read(3))


# print(sum(int(x) for x in open("./numbers.txt", "r")))
#
# file = open("./numbers.txt", "r")
# the_sum = 0
#
# for line in file:
#     the_sum += int(line)
#
# print(the_sum)


# text = '''[x for x in range(5)]'''
#
# print(eval(text))
# print([x for x in range(5)])
from tkinter.scrolledtext import example


# import os
#
#
# absolute_path = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(absolute_path, "words_count_files", "input.txt")
#
# print(file_path)
# file = open(file_path)
# print(file.read())

'''
with open("text.txt") as file:
    print(file.read())
 ------ is same ---------
file = open("text.txt")
print(file.read())
file.close
'''
with open("example.txt") as file:
    print(file.read())
print(file.read())

''' Work with .json files'''

# import json
#
# file = open("JavaScript_File.json")
# my_dictonary = json.load(file)
# print(type(my_dictonary))
# print(my_dictonary)
# for k, v in my_dictonary.items():
#     print(f"{k} -> {v}")
