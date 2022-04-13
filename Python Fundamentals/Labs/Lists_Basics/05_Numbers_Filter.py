# n = int(input())
#
# even_nums = []
# odd_nums = []
# positive_nums = []
# negative_nums = []
#
# for _ in range(n):
#     current_num = int(input())
#
#     if current_num % 2 == 0:
#         even_nums.append(current_num)
#     if current_num >= 0:
#         positive_nums.append(current_num)
#     if current_num % 2 == 1:
#         odd_nums.append(current_num)
#     if current_num < 0:
#         negative_nums.append(current_num)
#
# command = input()
#
# if command == "even":
#     print(even_nums)
# elif command == "odd":
#     print(odd_nums)
# elif command == "positive":
#     print(positive_nums)
# else:
#     print(negative_nums)




# n = int(input())
# numbers = []
# filtered = []
#
# for _ in range(n):
#     current_number = int(input())
#     numbers.append(current_number)
#
# command = input()
# if command == "even":
#     for number in numbers:
#         if number % 2 == 0:
#             filtered.append(number)
# elif command == "odd":
#     for number in numbers:
#         if number % 2 != 0:
#             filtered.append(number)
# elif command == "positive":
#     for number in numbers:
#         if number >= 0:
#             filtered.append(number)
# elif command == "negative":
#     for number in numbers:
#         if number < 0:
#             filtered.append(number)
# print(filtered)





# n = int(input())
# all_nums = []
#
# even_nums = []
# odd_nums = []
# positive_nums = []
# negative_nums = []
#
# for _ in range(n):
#     current_num = int(input())
#     all_nums.append(current_num)
#
# command = input()
# if command == "even":
#     for num in all_nums:
#         if num % 2 == 0:
#             even_nums.append(num)
#     print(even_nums)
# elif command == "positive":
#     for num in all_nums:
#         if num >= 0:
#             positive_nums.append(num)
#     print(positive_nums)
# elif command == "odd":
#     for num in all_nums:
#         if num % 2 == 1:
#             odd_nums.append(num)
#     print(odd_nums)
# else:
#     for num in all_nums:
#         if num < 0:
#             negative_nums.append(num)
#     print(negative_nums)



# number = int(input())
#
# numbers_list = list()
#
# for i in range(number):
#     current = int(input())
#     numbers_list.append(current)
#
# filter_word = input()
# filtered = list()
#
# for current_number in numbers_list:
#     if filter_word == "even":
#         if current_number % 2 == 0:
#             filtered.append(current_number)
#     if filter_word == "odd":
#         if current_number % 2 != 0:
#             filter_word.append(current_number)
#     if filter_word == "positive":
#         if current_number >= 0:
#             filtered.append(current_number)
#     if filter_word == "negative":
#         if filter_word < 0:
#             filtered.append(current_number)
# print(filtered)



number = int(input())
directed_commands = ["even", "odd", "positive", "negative"]

positive = list()
negative = list()
odd = []
even = []

for i in range(number):
    current = int(input())
    if current % 2 == 0:
        even.append(current)
    else:
        odd.append(current)
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)

filter_word = input()

if filter_word in directed_commands:
    print(eval(filter_word))
else:
    print(f"Positive : {positive}")
    print(f"Negative : {negative}")
    print(f"Even : {even}")
    print(f"ODD : {odd}")
# if filter_word == "even":
#     print(even)
# if filter_word == "odd":
#     print(odd)
# if filter_word == "positive":
#     print(positive)
# if filter_word == "negative":
#     print(negative)