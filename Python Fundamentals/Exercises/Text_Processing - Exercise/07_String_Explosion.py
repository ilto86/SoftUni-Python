# string = input()
# new_string = ""
# explosion = 0
#
# for index in range(len(string)):
#     if string[index] == ">":
#         explosion += int(string[index + 1])
#         new_string += string[index]
#     elif string[index] != ">" and explosion > 0:
#         explosion -= 1
#     else:
#         new_string += string[index]
#
#
# print(new_string)