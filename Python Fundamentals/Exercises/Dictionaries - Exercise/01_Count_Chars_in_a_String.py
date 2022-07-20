# data = input()
# word = []
# words = {}
#
# for index in data:
#     if index == " ":
#         continue
#     word.append(index)
#
# for char in word:
#     if char not in words:
#         words[char] = 0
#     words[char] += 1
#
# for key, value in words.items():
#     print(f"{key} -> {value}")



# given_string = input()
#
# str_dict = {}
#
# for letter in given_string:
#     if letter == ' ':
#         continue
#     if letter not in str_dict:
#         str_dict[letter] = 0
#     str_dict[letter] += 1
#
#
# for key,value in str_dict.items():
#     print(f'{key} -> {value}')



# data = input()
#
# words = {}
#
# for char in data:
#     if char == " ":
#         continue
#     if char not in words:
#         words[char] = 0
#     words[char] += 1
#
# [print(f'{key} -> {value}') for key, value in words.items()]
# # for key,value in words.items():
# #     print(f"{key} -> {value}")



# my_dict = {}
# word = input()
#
# for ch in word:
#     if ch != ' ':
#         if ch not in my_dict:
#             my_dict[ch] = 1
#         else:
#             my_dict[ch] += 1
# # [print(f'{key} -> {value}') for key, value in my_dict.items()]
# for key, value in my_dict.items():
#     print(f"{key} -> {value}")


from collections import Counter

word = input()
result = Counter(word)

for key, value in result.items():
    if key != ' ':
        print(f'{key} -> {value}')