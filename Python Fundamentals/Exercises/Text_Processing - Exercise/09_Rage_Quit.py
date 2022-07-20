# string = input().upper()
# manipulated_string = ""
# new_string = ""
#
# counter = 0
#
# while counter < len(string):
#     repeating = 0
#     if string[counter].isdigit():
#         if counter < len(string) - 1:
#             if string[counter + 1].isdigit():
#                 repeating += int(str(string[counter] + string[counter + 1]))
#                 manipulated_string = manipulated_string[:counter] * repeating
#                 new_string += manipulated_string
#                 manipulated_string = ""
#                 counter += 1
#             else:
#                 repeating += int(string[counter])
#                 manipulated_string = manipulated_string[:counter] * repeating
#                 new_string += manipulated_string
#                 manipulated_string = ""
#         else:
#             repeating += int(string[counter])
#             manipulated_string = manipulated_string[:counter] * repeating
#             new_string += manipulated_string
#             manipulated_string = ""
#     else:
#         manipulated_string += string[counter]
#
#     counter += 1
#
# all_symbols = set(new_string)
# print(f"Unique symbols used: {len(all_symbols)}")
# print(new_string)





# string = input().upper()
# manipulated_string = ""
# new_string = ""
#
# counter = 0
#
# while counter < len(string):
#
#     if string[counter].isdigit():
#         if counter < len(string) - 1:
#             if string[counter + 1].isdigit():
#                 new_string += (manipulated_string * int(str(string[counter] + string[counter + 1])))
#                 manipulated_string = ""
#                 counter += 1
#             else:
#                 new_string += manipulated_string * int(string[counter])
#                 manipulated_string = ""
#         else:
#             new_string += manipulated_string * int(string[counter])
#             manipulated_string = ""
#     else:
#         manipulated_string += string[counter]
#
#     counter += 1
#
# all_symbols = set(new_string)
# print(f"Unique symbols used: {len(all_symbols)}")
# print(new_string)









# string = input()
#
# manipulated_string = ''
# counter = ''
# new_string = ''
#
# for i in range(len(string)):
#     if string[i].isdigit():
#         repeater = string[i]
#         counter = i + 1
#         while counter < len(string) and string[counter].isdigit():
#             repeater += string[counter]
#             counter += 1
#         new_string += (manipulated_string.upper() * int(repeater))
#         manipulated_string = ''
#     else:
#         manipulated_string += string[i]
#
# all_symbols = set(new_string)
# print(f'Unique symbols used: {len(all_symbols)}')
# print(new_string)






# data = input()
# rage_quit = ""
#
# start = 0
# number = ""
# for index, char in enumerate(data):
# 	if char.isdigit():
# 		stop = index - len(number)
# 		number += char
# 		if index < len(data) - 1:
# 			if data[index + 1].isdigit():
# 				continue
# 		rage_quit += data[start:stop].upper() * int(number)
# 		start = stop + len(number)
# 		number = ""
#
# print(f"Unique symbols used: {len(set(rage_quit))}")
# print(rage_quit)


data = input().upper()
text = ""
final_result = ""

for i in range(len(data)):
	number = ""
	char = data[i]

	if not char.isdigit():
		text += char

	else:
		if i + 1 < len(data) and data[i + 1].isdigit():
			number = char + data[i + 1]
		else:
			number = char
		final_result += text * int(number)
		text = ""

print(f"Unique symbols used: {len(set(final_result))}")
print(f"{final_result}")